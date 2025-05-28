import pandas as pd
import os
import sys
import numpy
import datetime
from dataclasses import dataclass


from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    raw_data_path : str = os.path.join('data','data.csv')


class Ingestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        df = pd.read_csv(self.ingestion_config.raw_data_path, skiprows=5)
        return df
    
class CleanData:
    def __init__(self, data):
        self.data = data
    
    def clean_raw_data(self):
        df = self.data
        df = df.drop(['OrgId','ParticipantId', 'DeviceId'], axis = 1)
        df = df.drop_duplicates()
        df = df.dropna()
        df['eventtime'] = pd.to_datetime(df['eventtime'], errors='coerce')
        df = df.sort_values(by='eventtime', ascending=True)
        return df


