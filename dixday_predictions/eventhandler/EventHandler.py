import pandas as pd
from statsmodels.tsa.holtwinters import Holt
import traceback


class EventHandler:

    def __init__(self, return_func, config: dict):
        self.return_func = return_func
        self.temperatureData = pd.Series()
        self.MIN_TRAIN_DATA = config.get("MIN_TRAIN_DATA")  # TODO 100 ~60 sec
        self.DATA_TO_PREDICT = config.get("DATA_TO_PREDICT")  # TODO 100 ~30 sec
        self.FREQUENCY = config.get("FREQUENCY")  # TODO 30
        self.TEMPERATURE_KEY = config.get("TEMPERATURE_KEY")
        self.TIMESTAMP_KEY = config.get("TIMESTAMP_KEY")
        self.PREDICTION_KEY = config.get("PREDICTION_KEY")
        self.count = 0

    def on_event(self, data: dict, topic: str):
        try:
            predictions = self._handle_temperature_data(data)
            if predictions is not None:
                self.return_func({self.PREDICTION_KEY: predictions.to_list()})
        except Exception as e:
            traceback.print_tb(e)

    def _handle_temperature_data(self, data: dict):
        self.count = self.count + 1

        tempValue = data[self.TEMPERATURE_KEY]
        datetime = data[self.TIMESTAMP_KEY]

        datetime = pd.to_datetime(datetime, unit="ms")

        # append data point
        self.temperatureData[datetime] = tempValue
        # check if enough data available to train a model
        if(self.temperatureData.size > self.MIN_TRAIN_DATA):
            # reduce to the last MIN_TRAIN_DATA points
            self.temperatureData = self.temperatureData[-self.MIN_TRAIN_DATA:]

            # predict only each FREQUENCY steps
            if self.count % self.FREQUENCY == 0:
                return self.trainAndPredict(self.temperatureData)

    def trainAndPredict(self, series) -> pd.Series:
        # train Holt-winters model
        model = Holt(series)
        fit = model.fit(optimized=True)

        # predict defined nr of points
        return fit.forecast(self.DATA_TO_PREDICT)
