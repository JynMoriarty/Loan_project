import pickle
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

with open('xgb.pkl','rb') as file:
    xgb = pickle.load(file)

app = FastAPI()

class request(BaseModel):
    Industry: str
    Term : int
    NoEmp : int
    GrAppv : float
    NewExist : str
    CreateJob : int
    RetainedJob : int
    FranchiseCode : str
    UrbanRural : str
    Real_estate : str
    
@app.post("/predict")
    
def predict(data:request):
    new_data=pd.DataFrame(dict(data),index = [0])

    class_idx=xgb.predict(new_data)[0]
    return {'class':int(class_idx)}
