# task2
import requests
import csv

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
response.raise_for_status()
data = response.json()

print("------------------------------------------------------------")
print("|       Курс USD до UAH за тиждень                    |")
print("------------------------------------------------------------")
print("|     Дата встановлення     |     Курс до UAH              |")
print("|----------------------------|------------------------------|")

for row in data:
    date = row['exchangedate']
    rate = f"{row['rate']:.4f}"
    print(f"| {date:<26} | {rate:<28} |")

print("------------------------------------------------------------")

#  CSV
fields = ["exchangedate", "rate"]

with open("../../nbu_usd_20251025_20251101.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    for item in data:
        writer.writerow({k: item.get(k, "") for k in fields})

print("CSV-файл збережено як nbu_usd_20251025_20251101.csv")