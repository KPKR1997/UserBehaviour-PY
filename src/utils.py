import os
import sys
import matplotlib.pyplot as plt
from src.exception import CustomException
from src.logger import logging

class SaveChart:
    def __init__(self, folder="artifacts"):
        self.folder = folder
        os.makedirs(self.folder, exist_ok=True)

    def save(self, fig, filename=None, fmt="png"):
        
        if filename is None:
            filename = "Chart"

        full_path = os.path.join(self.folder, f"{filename}.{fmt}")
        try:
            fig.savefig(full_path, format=fmt, bbox_inches="tight")
            logging.info(f"Chart - {filename} saved to {full_path}")
        except Exception as e:
            raise CustomException(e,sys)
        plt.close(fig)
