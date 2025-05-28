import pandas as pd
import os
import sys
import numpy
import datetime

from src.exception import CustomException
from src.logger import logging

class Transformation:
    def __init__(self,data):
        self.data = data

    def transformation(self):
        