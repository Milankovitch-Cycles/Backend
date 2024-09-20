from pandas import DataFrame
from src.modules.time_series_predictor.time_series_predictor_service import TimeSeriesPredictorService
import optuna

class OptimizeTimeSeriesPredictorService:
    def __init__(self):
        self.optuna = optuna.create_study(direction='minimize')
        
    def objective(self, trial, dataframe: DataFrame):
        changepoint_prior_scale = trial.suggest_float('changepoint_prior_scale', 0.001, 0.5, step=0.001)
        seasonality_prior_scale = trial.suggest_float('seasonality_prior_scale', 0.01, 10, step=0.01)
        holidays_prior_scale = trial.suggest_float('holidays_prior_scale', 0.01, 10, step=0.01)
        changepoint_range = trial.suggest_float('changepoint_range', 0.8, 0.95, step=0.01)
        seasonality_mode = trial.suggest_categorical('seasonality_mode', ['additive', 'multiplicative'])

        predictor = TimeSeriesPredictorService(
            changepoint_prior_scale=changepoint_prior_scale, 
            seasonality_prior_scale=seasonality_prior_scale, 
            holidays_prior_scale=holidays_prior_scale, 
            changepoint_range=changepoint_range,
            seasonality_mode=seasonality_mode
        )
        
        return predictor.fit(dataframe)

    def fit(self, dataframe: DataFrame):
        self.optuna.optimize(lambda trial: self.objective(trial, dataframe), n_trials=100)
        self.model = TimeSeriesPredictorService(
            changepoint_prior_scale=self.optuna.best_params["changepoint_prior_scale"], 
            seasonality_prior_scale=self.optuna.best_params["seasonality_prior_scale"], 
            holidays_prior_scale=self.optuna.best_params["holidays_prior_scale"],
            changepoint_range=self.optuna.best_params["changepoint_range"],
            seasonality_mode=self.optuna.best_params.get("seasonality_mode", 'additive')
        )
        return self.model.fit(dataframe)

    def predict(self, dataframe: DataFrame):
        return self.model.predict(dataframe)