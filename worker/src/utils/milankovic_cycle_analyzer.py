import numpy as np
import pandas as pd
from scipy.signal import find_peaks

class MilankovitchCycleAnalyzer:
    @staticmethod
    def detect_cycles(dataframe: pd.DataFrame, tolerance: float) -> list:
        frequencies = np.array(dataframe['frequencies'])
        amplitudes = np.array(dataframe['amplitudes'])
        
        peaks, _ = find_peaks(amplitudes)
        
        dominant_periods = 1 / frequencies[peaks]
        dominant_amplitudes = amplitudes[peaks]
        
        milankovitch_periods = [
            {"type": "eccentricity", "period": 100_000},
            {"type": "obliquity", "period": 41_000},
            {"type": "precession", "period": 23_000}
        ]
        
        cycles_detected = {}
        
        for period in milankovitch_periods:
            cycle_period = period["period"]
            
            closest_index = np.argmin(np.abs(dominant_periods - cycle_period))
            closest_period = dominant_periods[closest_index]
            closest_amplitude = dominant_amplitudes[closest_index]
            
            error_percentage = np.abs(closest_period - cycle_period)/cycle_period*100
            
            if error_percentage <= tolerance:
                cycles_detected[period["type"]] = {
                    "detected": True,
                    "details": {
                        "period": int(closest_period),
                        "amplitude": int(closest_amplitude),
                        "error_percentage": error_percentage
                    }
                }
            else:
                cycles_detected[period["type"]] = {
                    "detected": False,
                    "details": {
                        "reason": "Frequency not within tolerance range"
                    }
                }
        
        return cycles_detected
