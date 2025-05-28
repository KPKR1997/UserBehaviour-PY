import pandas as pd
import os
import sys
import numpy
import datetime
import tldextract

from src.exception import CustomException
from src.logger import logging

class Transformation:
    def __init__(self,data):
        self.data = data

    def transform(self):
        df = self.data
        df['domain'] = df['url'].apply(lambda x: f"{tldextract.extract(x).domain}.{tldextract.extract(x).suffix}")
        df = df.drop('url', axis=1)
        
        
        def get_time_segment(dt):
            hour = dt.hour
            if 5 <= hour < 12:
                return 'Morning'
            elif 12 <= hour < 18:
                return 'Midday'
            else:
                return 'Night'
        df['time_of_day'] = df['eventtime'].apply(get_time_segment)
        


        df['prev_eventtime'] = df['eventtime'].shift(1)
        df['inactivity'] = (df['eventtime'] - df['prev_eventtime']).dt.total_seconds() / 60       
        df.drop(columns=['prev_eventtime'], inplace = True)
        print(df)
        return df