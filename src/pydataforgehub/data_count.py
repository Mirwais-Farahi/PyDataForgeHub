# src/data_counter.py

import pandas as pd

class DataCounter:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def count_by_column(self, column_name: str):
        """Count occurrences of each value in the specified column."""
        return self.df[column_name].value_counts()