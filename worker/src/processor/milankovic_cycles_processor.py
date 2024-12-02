import os
from pandas import DataFrame
from src.processor.job_processor import JobProcessor
from src.fourier_transform import FourierTransform
from src.milankovic_cycle_analyzer import MilankovitchCycleAnalyzer


class MilankovicCyclesProcessor(JobProcessor):
    def write_csv(self, dataframe: DataFrame, path: str):
        if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))       
        dataframe.to_csv(path, float_format='%.6f', index=False)
        return path
    
    def process(self, job, dataframe):
        tolerance = job.parameters.get("tolerance") or 4 # 4%
        sedimentation_rate = job.parameters.get("sedimentation_rate") or 0.001
        frequency_dataframe = FourierTransform.convert_to_frequency_domain(dataframe, "GR", sedimentation_rate)
        frequency_path = self.write_csv(frequency_dataframe, f"./static/{job.well_id}/{job.id}/frequencies.txt")
        cycles = MilankovitchCycleAnalyzer.detect_cycles(frequency_dataframe, tolerance)
        return {"frequencies_path": frequency_path, "cycles": cycles}