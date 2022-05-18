import requests
import random
from mission import function

headers= {
"apikey": "voM2ryIV9lZJZL8cPVPmqtfKv8y50YZd"
}

def call_API():
    latest_url = "https://api.apilayer.com/exchangerates_data/latest"
    response = requests.request("GET", latest_url, headers=headers)
    response = response.json()['rates']
    return response


def test_prod():
    retList = function()
    retDic = call_API()
    
    for i in retList:
        assert retDic[i] < 10
        

def test_dev():
    rand = random.random()
    retList = function(dev = True, rand = rand)
    retDic = call_API()
    
    for i in retList:    
        assert retDic[i] < rand

        
# for running pytest
# python -m pytest test_mission.py