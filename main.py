import requests
import time 
from datetime import datetime


WAIT_INTERVAL= 300 #seconds

#basic function that takes in email and if there is a breach returns a json file w/ it
#if not get fucked lol
def checkEmails(email):
    url= f'https://haveibeenpwned.com/api/v3/breachedaccount/{email}'
    header= {'User-Agent':'PythonClient\1.0'}
    resp= requests.get(url,header=header)

    if resp.status_code==200:
        return resp.json()
    elif resp.status_code==404:
        return None
    else:
        resp.raise_for_status()


