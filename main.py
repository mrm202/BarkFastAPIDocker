import os

os.environ["CUDA_VISIBLE_DEVICES"] = ""
os.environ["SUNO_USE_SMALL_MODELS"] = "1"

#from IPython.display import Audio
import numpy as np
import pandas as pd

from bark import generate_audio, preload_models, SAMPLE_RATE
from scipy.io.wavfile import write as write_wav
preload_models()

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class ScoringItem(BaseModel):
	TextPrompt:str # "Non-Manager", # Manager or Non-Manager

@app.post('/one')
async def scoring_endpoint(item:ScoringItem): 
    df = pd.DataFrame([item.dict().values()], columns=item.dict().keys())
    print(df['TextPrompt'][0])
    audio_array = generate_audio(df['TextPrompt'][0])
    # save audio to disk
    write_wav("bark_generation.wav", SAMPLE_RATE, audio_array)
    # play text in notebook
    #Audio(audio_array, rate=SAMPLE_RATE)
    return {"result":str(audio_array)}
    
    
@app.get("/")
async def root():
message = '''
	go to http://0.0.0.0:8005/docs
	'''
	
    return {"message": message}
