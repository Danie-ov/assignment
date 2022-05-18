import requests

def function(dev = False, rand = 0):
    headers= {
        "apikey": "voM2ryIV9lZJZL8cPVPmqtfKv8y50YZd"
    }
    latest_url = "https://api.apilayer.com/exchangerates_data/latest"
    response_var = requests.request("GET", latest_url, headers=headers)
    response_var = response_var.json()['rates']

    retList = []
    for key,value in response_var.items():
        #prod
        if not dev:    
            if value < 10:
                retList.append(key)
        else:
            #dev
            for key,value in response_var.items():
                if value < rand:
                    retList.append(key)

    return retList