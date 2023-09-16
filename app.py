from src.Pipeline.predict_pipe import  Predict_Pipeline

if __name__ == "__main__":
    obj = Predict_Pipeline()
    print(obj.predict(gender = "female",
        race_ethnicity="group C",
        parental_level_of_education="bachelor's degree",
        lunch= "free/reduced",
        test_preparation_course="none",
        reading_score= 75,
        writing_score= 60))