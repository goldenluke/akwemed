from fastapi import FastAPI
from pydantic import BaseModel
from core.clinical.assistant import ClinicalAssistant

app = FastAPI()

assistant = ClinicalAssistant()

class Query(BaseModel):

    text:str

@app.post("/consult")

def consult(q:Query):

    return assistant.consult(q.text)
