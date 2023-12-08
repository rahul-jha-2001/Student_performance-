The project is centered around a dataset discovered on Kaggle. It commenced with the customary Exploratory Data Analysis (EDA), preprocessing, and the development of various models, followed by a comparative analysis of their performance. Upon completing these tasks in Jupyter, I proceeded to script the data ingestion, data preprocessing, and prediction pipeline for the model.

In the data ingestion phase, a CSV file was constructed, easily configurable to retrieve data from alternative sources. The data transformation stage involved processing the data through a pipeline that incorporated methods identified during EDA, such as imputers, scaling, and the vectorization of categorical variables. This segment also generated an object file used in preprocessing, subsequently utilized in the prediction pipeline.

The model-building aspect was dedicated to identifying the most suitable model with optimal parameters, determined through grid search from a predefined selection of models. This phase culminated in the creation of an object file for the best-performing model.

Finally, the predict pipeline, equipped with a user-friendly interface developed using Gradio, takes input from the user and executes the necessary transformations using the object files generated in the data transformation stage.
