import pandas as pd
import numpy as np
import os
import sys

from src.exception import CustomException
from src.logger import logging
from src.components.Ingestion import Ingestion
from src.components.Ingestion import CleanData



if __name__ == "__main__":
    data_ingestion = Ingestion()
    raw_df = data_ingestion.initiate_data_ingestion()
    clean_data = CleanData(raw_df)
    clean_df = clean_data.clean_raw_data()
    print(raw_df)