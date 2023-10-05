import gradio as gr
import os
import requests

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from modules import script_callbacks

extensions_path = __file__.split("/extensions",1)[0]
self_folder = os.path.join(extensions_path,"extensions/sd_callInterface")
with open(os.path.join(self_folder,"easy_ui.html"),"r") as f:
    callInterface_html = f.read()

def on_ui_tabs():
    with gr.Blocks(analytics_enabled=False) as ui_component:
        with gr.Column():
            pass
        return [(ui_component, "callInterface", "callInterface")]
    
def on_app_started(_: gr.Blocks, app: FastAPI) -> None:
    @app.get("/callInterface/easy_ui.html",response_class=HTMLResponse)
    def welcome():
        return callInterface_html

    @app.post("/callInterface/api/txt2img")
    def callInterface(data:dict):
        response = requests.post("http://127.0.0.1:7860/sdapi/v1/txt2img",json=data)
        if response.status_code == 200:
            return response.json()["images"][0]
        raise ConnectionError
    @app.get("/callInterface/api/upscaler")
    def getUpscaler():
        response = requests.get("http://127.0.0.1:7860/sdapi/v1/upscalers")
        if response.status_code == 200:
            return ",".join([upscaler for upscaler in response.json() if upscaler["name"] !="None"])
script_callbacks.on_ui_tabs(on_ui_tabs)
script_callbacks.on_app_started(on_app_started)
