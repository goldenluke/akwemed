from celery import shared_task
import requests

AI_URL = "http://localhost:9000/consult"

@shared_task
def async_consult(text):

    r = requests.post(AI_URL,json={"text":text})

    return r.json()
