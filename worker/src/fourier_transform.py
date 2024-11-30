import pandas as pd
import numpy as np

class FourierTransform:
    @staticmethod
    def convert_to_frequency_domain(
        dataframe: pd.DataFrame, column: str, sedimentation_rate: float
    ) -> pd.DataFrame:
        dataframe = dataframe.dropna(subset=[column])

        column_array = dataframe[column].to_numpy()
        depth = dataframe.index.to_numpy()

        time = depth / sedimentation_rate

        fft_values = np.fft.fft(column_array)
        frequencies = np.fft.fftfreq(len(column_array), d=(time[1] - time[0]))

        half_size = len(column_array) // 2
        positive_amplitudes = np.abs(fft_values[:half_size])
        positive_frequencies = frequencies[:half_size]

        return pd.DataFrame(
            {"frequencies": positive_frequencies, "amplitudes": positive_amplitudes}
        )


