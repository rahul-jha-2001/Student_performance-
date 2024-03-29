import os
import sys

import numpy as np 
import pandas as pd
import dill
import pickle
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException

def eval_model(true, predicted):
    r2_square = r2_score(true, predicted)
    return r2_square


def save_object(file_path , obj):
        try:
            dir_path = os.path.dirname(file_path)

            os.makedirs(dir_path,exist_ok= True)

            with open(file_path,"wb") as file_obj:
                  pickle.dump(obj,file_obj)
        except Exception as e:
              raise CustomException(e,sys)
def load_Obj(file_path):
        try:
            with open(file_path,"rb") as file_obj:
                  return dill.load(file_obj)
        except Exception as e:
              raise CustomException(e,sys)        
        
        
def evaluate_model(X,Y,X_test,Y_test,Models,Param):
    try:
        report = {}
        for i in range(len(list(Models))):
            model = list(Models.values())[i]
            para  = Param[list(Models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X,Y)

            model.set_params(**gs.best_params_)
            model.fit(X,Y)

            # Make predictions
            y_train_pred = model.predict(X)
            y_test_pred = model.predict(X_test)
            
            # Evaluate Train and Test dataset
            model_test_r2 = eval_model(Y_test, y_test_pred)
            
            report[(list(Models.keys())[i])] = model_test_r2
        return report

    except Exception as e:
        raise CustomException(e,sys)
        