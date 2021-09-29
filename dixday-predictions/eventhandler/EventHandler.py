import pandas as pd
from statsmodels.tsa.holtwinters import Holt
import traceback


class EventHandler:

    def __init__(self, return_func):
        self.return_func = return_func
        self.temperatureData = pd.Series()
        self.MIN_TRAIN_DATA = 100  # TODO ~60 sec
        self.DATA_TO_PREDICT = 100  # TODO ~30 sec
        self.TEMPERATURE_THRESHOLD = 27.0  # TODO
        self.FREQUENCY = 30  # TODO
        self.count = 0

    def on_event(self, data: dict, topic: str):
        try:
            self._handle_temperature_data(data)
        except Exception as e:
            traceback.print_tb(e)
        # TODO:
        # self.return_func(data)

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
                self.trainAndPredict(self.temperatureData)

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
