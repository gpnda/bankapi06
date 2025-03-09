import gspread
from oauth2client.service_account import ServiceAccountCredentials
#from google.oauth2.service_account import Credentials
import json

# Читаем файл конфигурации
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)




gc = gspread.service_account(filename="./credentials.json")
sh = gc.open("api2025")
print("RESULT: ")
print(sh.sheet1.acell('A1').value)





tokenfile_path = './tinkoff-token.txt'
with open(tokenfile_path, 'r', encoding='utf-8') as file:
    tinkoff_token = file.read()

import http.client
conn = http.client.HTTPSConnection("business.tbank.ru")
payload = ''
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer ' + config['tinkoff']['token'] + ''
}
conn.request("GET", "/openapi/api/v1/statement?accountNumber="+config['tinkoff']['account']+"&from=2022-02-01T21:00:00Z", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


