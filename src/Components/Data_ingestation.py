import os
import sys 
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class Data_ingestion_config:
    train_data_path: str =  os.path.join("artifact","train.csv")
    test_data_path: str =  os.path.join("artifact","test.csv")
    raw_data_path: str =  os.path.join("artifact","raw.csv")

class Data_ingestion:
    def __init__(self):
        self.ingestion_config =  Data_ingestion_config()

    def intiate_data_ingestion(self):
        logging.info("Entered the data ingestation method or component")
        try:
            df = pd.read_csv("data.csv")
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok= True) 
            
            df.to_csv(self.ingestion_config.raw_data_path,index = False,header = True)
            logging.info("Train_test_split intiated")

            train_set,test_set = train_test_split(df,test_size=0.2,random_state= 1)

            train_set.to_csv(self.ingestion_config.train_data_path,index = False,header = True)
            test_set.to_csv(self.ingestion_config.test_data_path,index = False,header = True)

            logging.info("Ingestion of data is done")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__ == "__main__":
    obj =  Data_ingestion()
    obj.intiate_data_ingestion() 

        

                
