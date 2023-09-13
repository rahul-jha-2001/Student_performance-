import sys 
import pandas as pd 
import numpy as  np
import os
from dataclasses import dataclass
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging

from Data_ingestation import Data_ingestion

@dataclass

class Data_transformation_config:
    Preprpcessor_obj_file = os.path.join("artifact","Preprocessor.pkl")

class Data_transformation:
    def __init__(self) -> None:
        self.data_transformation_config =  Data_transformation_config()
    def get_data_transformer_object(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)



