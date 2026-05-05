"""data ingestion module"""

import os
import pandas as pd


os.makedirs('data', exist_ok=True)


class DataIngestion:
    
    def __init__(self, data_dict: dict) -> dict:
        self.data_dict = data_dict

    def get_data(self) -> pd.DataFrame:
        """returns Data Frame"""

        return pd.DataFrame(self.data_dict)

    def save_data(self, path: str) -> None:
        """saves data as CSV"""

        self.get_data().to_csv(path)

if __name__ == "__main__":

    data_dict = {'Name':['Hrithik', 'Shannon', 'Niamh'],
                 'Role':['MLOps Engineer', 'AI Engineer', 'Data Scientist']}

    ingestion = DataIngestion(data_dict=data_dict)
    print(ingestion.save_data(os.path.join(os.getcwd()+"/data/data.csv")))
