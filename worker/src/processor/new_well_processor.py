import os
from pandas import DataFrame
from src.processor.job_processor import JobProcessor

        
class NewWellProcessor(JobProcessor):
    def write_csv(self, dataframe: DataFrame, path: str):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))       
        numeric_dataframe = dataframe.select_dtypes(include=['int'])
        variation = numeric_dataframe.diff().abs().sum(axis=1)
        representative_dataframe = dataframe.loc[variation.nlargest(200).index]
        representative_dataframe.to_csv(path, float_format='%.0f')
        return path
    
    def process(self, job, dataframe):
        dataframe['TEMP_DEPTH'] = dataframe.index.astype(int)
        dataframe['GR'] = dataframe['GR'].dropna().astype(int)
        dataframe = dataframe.groupby('TEMP_DEPTH').mean()
        gamma_ray_path = self.write_csv(dataframe[['GR']], f"./static/{job.well_id}/gamma_ray.txt")
        return {"gamma_ray_path": gamma_ray_path}