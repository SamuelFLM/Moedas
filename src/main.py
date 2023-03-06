import requests


# req = requests.get("https://cep-static.awesomeapi.com.br/json/30230522")
# dic = req.json()

req = requests.get("http://economia.awesomeapi.com.br/json/last/CAD-CLP")
dic = req.json()
print(dic)