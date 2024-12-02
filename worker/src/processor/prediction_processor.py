import os
from pandas import DataFrame
from src.processor.job_processor import JobProcessor

        
class PredictionProcessor(JobProcessor):
    def write_csv(self, dataframe: DataFrame, path: str):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))       
        variation = dataframe.diff().abs().sum(axis=1)
        representative_dataframe = dataframe.loc[variation.nlargest(200).index].sort_values('TEMP_DEPTH', ascending=True)
        representative_dataframe.to_csv(path, float_format='%.4f')
        return path
    
    def normalize_min(self, min: float, max: float, value: float):
        if(value < min):
            return 0
        elif(value > max):
            return 1
        return (abs(value - min) / abs(max - min))
    
    def normalize_max(self, min: float, max: float, value: float):
        return 1 - self.normalize_min(min, max, value)
    
    def process(self, job, dataframe):
        predictions_dataframe = dataframe.copy()
        predictions_dataframe['OIL_PROBABILITY'] = (
            0.2*dataframe['GR'].apply(lambda x: self.normalize_max(50, 100, x)) +
            0.2*dataframe['NEU'].apply(lambda x: self.normalize_min(10, 30, x)) +
            0.2*dataframe['RDEP'].apply(lambda x: self.normalize_min(20, 100, x)) +
            0.2*dataframe['DEN'].apply(lambda x: self.normalize_max(2.2, 2.65, x)) +
            0.2*dataframe['AC'].apply(lambda x: self.normalize_min(70, 100, x))
        )
        predictions_dataframe['TEMP_DEPTH'] = predictions_dataframe.index.astype(int)
        predictions_dataframe = predictions_dataframe.groupby('TEMP_DEPTH').mean()
        predictions_path = self.write_csv(predictions_dataframe[['OIL_PROBABILITY']], f"./static/{job.well_id}/{job.id}/prediction.txt")
        return {"predictions_path": predictions_path}
