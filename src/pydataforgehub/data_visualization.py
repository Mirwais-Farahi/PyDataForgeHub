# src/data_visualization.py

import pandas as pd
import matplotlib.pyplot as plt

class DataVisualizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def plot_histogram(self, column_name: str):
        """Plot a histogram of the specified column."""
        self.df[column_name].hist()
        plt.show()