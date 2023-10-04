import gradio as gr
import os
import requests

from fastapi import FastAPI

from modules import script_callbacks

self_folder = __file__.rsplit("/",1)[1]
with open(os.path.join(self_folder,"easy_ui.html"),"r") as f:
    callInterface_html = f.read()

extensions_path = self_folder.split("/extensions",1)[0]

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Column():
            pass
        return [(ui_component, "callInterface", "callInterface")]
    
def on_app_started(_: gr.Blocks, app: FastAPI) -> None:
    @app.get("/callInterface/easy_ui.html")
    def welcome():
        return callInterface_html

    @app.post("/callInterface/api/txt2img")
    def callInterface(data:dict):
        response = requests.post("http://127.0.0.1:7860/sdapi/v1/txt2img",json=data)
        if response.status_code == 200:
            return response.json()["images"][0]
        raise ConnectionError

script_callbacks.on_ui_tabs(on_ui_tabs)
script_callbacks.on_app_started(on_app_started)
