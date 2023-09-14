# Basic Import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os
# Modelling
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,AdaBoostRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression, Ridge,Lasso
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.model_selection import RandomizedSearchCV
from catboost import CatBoostRegressor
from xgboost import XGBRegressor
import warnings
import sys
from dataclasses import dataclass
from src.utils import save_object,evaluate_model
from src.logger import logging
from src.exception import CustomException


@dataclass

class Model_training_config:
    trained_model_path = os.path.join("artifacts","model.pkl")
class Model_trainer:
    def __init__(self) -> None:
        self.model_trainer_config = Model_training_config()
    
    def intiate_model_trainer(self,train_array,test_array):
        try:
            logging.info("Split training and testing data ")
            x_train,y_train,x_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models = {
                "Random Forest":RandomForestRegressor(),
                "Decision tree" : DecisionTreeRegressor(),
                "Linear Regression" : LinearRegression(),
                "K-neighbors Classifier": KNeighborsRegressor(),
                "XGBClassifier": XGBRegressor(),
                "Catboosting Classifier":CatBoostRegressor(),
                "AdaBoost Classifer":AdaBoostRegressor()
            }
            model_report:dict = evaluate_model(X=x_train,Y = y_train,X_test = x_test,Y_test=y_test,Models = models)

            best_model_score = max(sorted(model_report.values()))

            best_model_nm = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            best_model =  models[best_model_nm]
            if best_model_score < 0.6:
                raise CustomException("No best model found")
            logging.info("Best model Found")

            save_object(file_path= Model_training_config.trained_model_path,
                        obj = best_model )
            predicted = best_model.predict(x_test)
            r2score = r2_score(y_test,predicted) 
            return r2score
            
        except Exception as e:
            raise CustomException(e,sys)
        

