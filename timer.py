import os
import requests
from datetime import datetime
from time import sleep

def loadTime():
    try:
        response  = requests.get('https://worldtimeapi.org/api/timezone/America/Sao_paulo')
        responseJson =  response.json()
        datetimeJson = responseJson.get('datetime')
        datetimeFormated = datetime.fromisoformat(datetimeJson)
        os.system(f'date {datetimeFormated.strftime("%d-%m-%Y")}')
        os.system(f'time {datetimeFormated.strftime("%H:%M")}')
    except:
        sleep(1)
        loadTime()
        
loadTime()
