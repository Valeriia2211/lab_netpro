# task3
import requests
import matplotlib.pyplot as plt
from datetime import datetime

url = "https://bank.gov.ua/NBU_Exchange/exchange_site"

params = {
    "start": "20251025",
    "end": "20251101",
    "valcode": "usd",
    "sort": "exchangedate",
    "order": "asc",
    "json": ""
}

response = requests.get(url, params=params)
data = response.json()

# Масиви для графіка
dates = []
rates = []

for row in data:
    date_obj = datetime.strptime(row["exchangedate"], "%d.%m.%Y")
    dates.append(date_obj)
    rates.append(float(row["rate"]))

# Побудова графіка
plt.figure(figsize=(10,5))
plt.plot(dates, rates, marker="o")
plt.title("Зміна курсу USD (НБУ)\n25.10.2025 – 01.11.2025")
plt.xlabel("Дата")
plt.ylabel("Курс UAH за USD")
plt.grid(True)
plt.tight_layout()
plt.show()
