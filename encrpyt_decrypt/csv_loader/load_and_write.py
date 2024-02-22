import pandas as pd

class CsvHandler:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
    
    def read_csv(self):
        df = pd.read_csv(self.input_path)
        return df
    
    