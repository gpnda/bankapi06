import json
# Читаем файл конфигурации
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)



import requests
url = "https://enter.tochka.com/uapi/open-banking/v1.0/accounts/40802810820000393689/044525104/balances"
payload = {}
headers = {
'Authorization': 'Bearer '+config['tochka']['token']
}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)


















