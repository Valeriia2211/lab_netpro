from flask import Flask, request
import requests
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route("/currency")
def get_nbu():

    days = 0 if 'today' in request.args else 1
    date = (datetime.now() - timedelta(days=days)).strftime("%Y%m%d")

    url = f"https://bank.gov.ua/NBUStatService/v1/statistictbl/exchange?valcode=USD&date={date}&json"

    try:
        res = requests.get(url).json()
        if not res:
            date = (datetime.now() - timedelta(days=1)).strftime("%Y%m%d")
            res = requests.get(url.replace(datetime.now().strftime("%Y%m%d"), date)).json()

        rate = res[0]['rate']
        return f"Курс USD за {date}: {rate}"
    except:
        return "Сервіс НБУ тимчасово недоступний"


if __name__ == '__main__':
    app.run(port=8000)