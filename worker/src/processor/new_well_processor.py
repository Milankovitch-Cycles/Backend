import os
import pandas as pd
from pandas import DataFrame
from src.processor.job_processor import JobProcessor

class NewWellProcessor(JobProcessor):
    def write_csv(self, dataframe: DataFrame, path: str):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))       
        dataframe.to_csv(path, float_format='%.2f', index=False)
        return path

    def process(self, job, dataframe, step = 20):
        gamma_ray_dataframe = dataframe[['GR']].dropna().copy()
        gamma_ray_dataframe['TEMP_DEPTH'] = gamma_ray_dataframe.index.astype(int)
        gamma_ray_dataframe['GROUP'] = (gamma_ray_dataframe['TEMP_DEPTH'] // step).astype(int)
        averaged_dataframe = gamma_ray_dataframe.groupby('GROUP').apply(
            lambda group: {
                'TEMP_DEPTH': int(group['TEMP_DEPTH'].iloc[0]),
                'GR': int(group['GR'].mean())
            }
        ).apply(pd.Series).reset_index(drop=True)
        gamma_ray_path = self.write_csv(averaged_dataframe, f"./static/{job.well_id}/gamma_ray.txt")
        return {"gamma_ray_path": gamma_ray_path}