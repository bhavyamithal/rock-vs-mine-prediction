import uvicorn
from fastapi import FastAPI
from rockClsf import RockClsf
import numpy as np
import pickle
import pandas as pd

app = FastAPI()
pickle_in = open("model.pkl","rb")
rockClsf = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome to my world': f'{name}'}

@app.post('/predict')
def predict_rock(data:RockClsf):
    data = data.dict()
    one = data['one']
    two = data['two']
    three = data['three']
    four = data['four']
    five = data['five']
    six = data['six']
    seven = data['seven']
    eight = data['eight']
    nine = data['nine']
    ten = data['ten']
    eleven = data['eleven']
    twelve = data['twelve']
    thirteen = data['thirteen']
    fourteen = data['fourteen']
    fifteen = data['fifteen']
    sixteen = data['sixteen']
    seventeen = data['seventeen']
    eighteen = data['eighteen']
    nineteen = data['nineteen']
    twenty = data['twenty']
    twentyone = data['twentyone']
    twentytwo = data['twentytwo']
    twentythree = data['twentythree']
    twentyfour = data['twentyfour']
    twentyfive = data['twentyfive']
    twentysix = data['twentysix']
    twentyseven = data['twentyseven']
    twentyeight = data['twentyeight']
    twentynine = data['twentynine']
    thirty = data['thirty']
    thirtyone = data['thirtyone']
    thirtytwo = data['thirtytwo']
    thirtythree = data['thirtythree']
    thirtyfour = data['thirtyfour']
    thirtyfive = data['thirtyfive']
    thirtysix = data['thirtysix']
    thirtyseven = data['thirtyseven']
    thirtyeight = data['thirtyeight']
    thirtynine = data['thirtynine']
    forty = data['forty']
    fortyone = data['fortyone']
    fortytwo = data['fortytwo']
    fortythree = data['fortythree']
    fortyfour = data['fortyfour']
    fortyfive = data['fortyfive']
    fortysix = data['fortysix']
    fortyseven = data['fortyseven']
    fortyeight = data['fortyeight']
    fortynine = data['fortynine']
    fifty = data['fifty']
    fiftyone = data['fiftyone']
    fiftytwo = data['fiftytwo']
    fiftythree = data['fiftythree']
    fiftyfour = data['fiftyfour']
    fiftyfive = data['fiftyfive']
    fiftysix = data['fiftysix']
    fiftyseven = data['fiftyseven']
    fiftyeight = data['fiftyeight']
    fiftynine = data['fiftynine']
    sixty = data['sixty']
    prediction = rockClsf.predict([[one, two, three, four, five,
                                     six, seven, eight, nine, ten,
                                     eleven, twelve, thirteen, fourteen, fifteen,
                                     sixteen, seventeen, eighteen, nineteen, twenty,
                                     twentyone, twentytwo, twentythree, twentyfour, twentyfive,
                                     twentysix, twentyseven, twentyeight, twentynine, thirty,
                                     thirtyone, thirtytwo, thirtythree, thirtyfour, thirtyfive,
                                     thirtysix, thirtyseven, thirtyeight, thirtynine, forty,
                                     fortyone, fortytwo, fortythree, fortyfour, fortyfive,
                                     fortysix, fortyseven, fortyeight, fortynine, fifty,
                                     fiftyone, fiftytwo, fiftythree, fiftyfour, fiftyfive,
                                     fiftysix, fiftyseven, fiftyeight, fiftynine, sixty
                                     ]])
    if(prediction[0] == 1):
        prediction = 'Rock'
    else:
        prediction = 'Mine'
    return {
        'prediction': prediction
    }