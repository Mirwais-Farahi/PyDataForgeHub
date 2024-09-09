# src/data_analysis.py

import pandas as pd

class DataAnalyzer:
    def __init__(self, df: pd.DataFrame):
        self.df = df
    
    def correlation_between(self, column1: str, column2: str):
        """Calculate the correlation between two columns."""
        return self.df[column1].corr(self.df[column2])