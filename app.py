from src.Pipeline.predict_pipe import  Predict_Pipeline
import gradio as gr
from src.exception import CustomException

obj = Predict_Pipeline()

demo = gr.Interface(obj.predict,
    inputs= [
        gr.Radio(["male","female"],label="Gender"),
        gr.Dropdown(['group B' ,'group C' ,'group A' ,'group D' ,'group E'],label="Race"),
        gr.Dropdown(["bachelor's degree" ,'some college' ,"master's degree", "associate's degree",
 'high school' ,'some high school'],label="Parent Education"),
        gr.Radio(['standard', 'free/reduced'],label="Lunch"),
        gr.Radio(['none', 'completed'],label="Coaching"),
        gr.Slider(0,100,label="writing Score"),
        gr.Slider(0,100,label="reading score")],
        outputs = "number"
            )   



if __name__ == "__main__":   
    demo.launch()