from src.utils import load_Obj
from src.utils import CustomException

import sys
import pandas as pd



class Predict_Pipeline():
    model_path = "artifact/model.pkl"
    preprocessor_path = "artifact/Preprocessor.pkl"
    def __init__(self):
        print("model is loading")
        self.model =  load_Obj(self.model_path)
        self.preprocessor =  load_Obj(self.preprocessor_path)
        print("model is loaded")
    def predict(self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education:str,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):
        print("data is loading ")
        data = CustomData(
        gender,
        race_ethnicity,
        parental_level_of_education,
        lunch,
        test_preparation_course,
        reading_score,
        writing_score).get_data_as_data_frame()
        print("data is loaded")
        data_scaled =  self.preprocessor.transform(data)
        pred =  self.model.predict(data_scaled)
        print("prediction done")
        return pred
class CustomData:
    def __init__(  self,
        gender: str,
        race_ethnicity: str,
        parental_level_of_education,
        lunch: str,
        test_preparation_course: str,
        reading_score: int,
        writing_score: int):

        self.gender = gender

        self.race_ethnicity = race_ethnicity

        self.parental_level_of_education = parental_level_of_education

        self.lunch = lunch

        self.test_preparation_course = test_preparation_course

        self.reading_score = reading_score

        self.writing_score = writing_score

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)

