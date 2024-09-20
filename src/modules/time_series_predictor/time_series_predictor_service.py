from pandas import DataFrame
from prophet import Prophet
from sklearn.metrics import mean_absolute_percentage_error

class TimeSeriesPredictorService:
    def __init__(self, changepoint_prior_scale, seasonality_prior_scale, holidays_prior_scale, changepoint_range=0.8, seasonality_mode='additive'):
        self.prophet = Prophet(
            changepoint_prior_scale=changepoint_prior_scale,
            seasonality_prior_scale=seasonality_prior_scale,
            holidays_prior_scale=holidays_prior_scale,
            changepoint_range=changepoint_range,
            seasonality_mode=seasonality_mode
        )

    def prepare_dataframes(self, dataframe: DataFrame):
        dataframe_size = len(dataframe)  
        testing_dataframe_size = int(dataframe_size * 0.8) 

        training_dataframe = dataframe[0:testing_dataframe_size]
        testing_dataframe = dataframe[testing_dataframe_size:dataframe_size]  
        prediction_dataframe = testing_dataframe.drop(columns=["y"])

        return training_dataframe, testing_dataframe, prediction_dataframe

    def fit(self, dataframe: DataFrame):
        training_dataframe, testing_dataframe, prediction_dataframe = self.prepare_dataframes(dataframe)

        self.prophet.fit(training_dataframe)
        predicted_dataframe = self.prophet.predict(prediction_dataframe)
        
        predicted_values = predicted_dataframe["yhat"].values
        testing_values = testing_dataframe["y"].values

        mape = mean_absolute_percentage_error(testing_values, predicted_values)
        return mape

    def predict(self, dataframe: DataFrame):
        return self.prophet.predict(dataframe)