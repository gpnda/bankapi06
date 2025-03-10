import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# Читаем файл конфигурации
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)




gc = gspread.service_account(filename="./credentials.json")
sh = gc.open("api2025")
print("RESULT: ")
print(sh.sheet1.acell('A1').value)
sh.sheet1.update_cell(1, 1, 'Bingo!')







import http.client
conn = http.client.HTTPSConnection("business.tbank.ru")
payload = ''
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer ' + config['tinkoff']['token'] + ''
}
conn.request("GET", "/openapi/api/v1/statement?accountNumber="+config['tinkoff']['account']+"&from=2024-01-01T00:00:00Z", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))


datajson = json.loads(data.decode("utf-8"))





all_operations = []
for i, value in enumerate(datajson['operations'], start=1):
    if(value['typeOfOperation'] == 'Debit'):
        rubleAmount = value['rubleAmount']*(-1)
    elif (value['typeOfOperation'] == 'Credit'):
        rubleAmount = value['rubleAmount']
    else:
        rubleAmount = 'Error: typeOfOperation'
    all_operations.append([
        value['operationId'] , 
        value['operationDate'],
        rubleAmount,
        'ТИНЬКОФФ ОСНОВНОЙ Р/С',
        ' ',
        value['counterParty']['name'],
        value['description'],
        ' '
        ])
    
# "": "Debit"
sh.sheet1.update([
    ['ID операции', 'Дата', 'Сумма', 'Кошелек', 'Направление бизнеса', 'Контрагент', 'Назначение платежа', 'Статья'],
], 'A1:H1')
sh.sheet1.update(all_operations, 'A2:H10000')



# Получаем данные с банка в JSON объект
# Цикл по всем полученных операциям 
#     Построчно собираем в список списков
# Обновляем список списков сразу во Range

