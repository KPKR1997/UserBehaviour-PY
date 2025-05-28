import pandas as pd
import numpy as np
import os
import sys

from src.exception import CustomException
from src.logger import logging
from src.components.Ingestion import Ingestion
from src.components.Ingestion import CleanData
from src.components.chart_generation import chartGenerator
from src.components.transformation import Transformation



if __name__ == "__main__":
    data_ingestion = Ingestion()
    raw_df = data_ingestion.initiate_data_ingestion()
    clean_data = CleanData(raw_df)
    clean_df = clean_data.clean_raw_data()
    transform_data = Transformation(clean_df)
    ready_data = transform_data.transform()
    generate_chart = chartGenerator(ready_data)
    generate_chart.barchart_of_titles(10)
    generate_chart.user_activity_time()
    generate_chart.domains_after_inactivity(240)
    generate_chart.most_typed_domains()