import pandas as pd
from statsmodels.tsa.holtwinters import Holt
import traceback


class EventHandler:

    def __init__(self, return_func, config):
        self.return_func = return_func
        self.temperatureData = pd.Series()
        self.MIN_TRAIN_DATA = config["MIN_TRAIN_DATA"]  # TODO 100 ~60 sec
        self.DATA_TO_PREDICT = config["DATA_TO_PREDICT"]  # TODO 100 ~30 sec
        self.TEMPERATURE_THRESHOLD = config["TEMPERATURE_THRESHOLD"]  # TODO 27.0
        self.FREQUENCY = config["FREQUENCY"]  # TODO 30
        self.count = 0

    def on_event(self, data: dict, topic: str):
        try:
            state = self._handle_temperature_data(data)
            if state:
                self.return_func({"state": state})
        except Exception as e:
            traceback.print_tb(e)

    def _handle_temperature_data(self, data: dict):
        self.count = self.count + 1

        # TODO adjust keys
        tempValue = data["temp"]
        datetime = data["time"]

        # append data point
        self.temperatureData[datetime] = tempValue

        # check if enough data available to train a model
        if(self.temperatureData.size > self.MIN_TRAIN_DATA):
            # reduce to the last MIN_TRAIN_DATA points
            self.temperatureData = self.temperatureData[-self.MIN_TRAIN_DATA:]

            # predict only each FREQUENCY steps
            if self.count % self.FREQUENCY == 0:
                return self.trainAndPredict(self.temperatureData)

    def trainAndPredict(self, series):
        # train Holt-winters model
        model = Holt(series)
        fit = model.fit(optimized=True)

        # predict defined nr of points
        pred = fit.forecast(self.DATA_TO_PREDICT)

        # check if THRESHOLD will be reached
        if(pred.max() >= self.TEMPERATURE_THRESHOLD):
            return 1
        else:
            return 0
