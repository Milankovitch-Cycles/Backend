import numpy as np
import pandas as pd
from scipy.signal import find_peaks

class MilankovitchCycleAnalyzer:
    @staticmethod
    def detect_cycles(dataframe: pd.DataFrame) -> list:
        frequencies = np.array(dataframe['frequencies'])
        amplitudes = np.array(dataframe['amplitudes'])
        
        peaks, _ = find_peaks(amplitudes, height=5000)
        
        dominant_periods = 1 / frequencies[peaks]
        dominant_amplitudes = amplitudes[peaks]
        
        milankovitch_periods = [
            {"type": "eccentricity", "period": 100_000},
            {"type": "obliquity", "period": 41_000},
            {"type": "precession", "period": 23_000}
        ]
        
        cycles_detected = []
        
        for period in milankovitch_periods:
            closest_index = np.argmin(np.abs(dominant_periods - period["period"]))
            closest_period = dominant_periods[closest_index]
            closest_amplitude = dominant_amplitudes[closest_index]
            
            cycles_detected.append({
                "type": period["type"],
                "period": int(closest_period),
                "amplitude": int(closest_amplitude)
            })
        
        return cycles_detected
