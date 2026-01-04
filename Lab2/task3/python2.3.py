from flask import Flask, request

app = Flask(__name__)


# Додаємо обробку головної сторінки, щоб не було 404
@app.route('/')
def index():
    return "Вітаю! Перейдіть на /currency, щоб побачити курс."


@app.route('/currency')
def get_currency():
    # Отримуємо параметри
    today = request.args.get('today')
    key = request.args.get('key')

    # Логування в консоль (ви побачите це в PyCharm)
    print(f"Отримано параметри: today={today}, key={key}")

    return "USD - 41,5"


if __name__ == '__main__':
    # Переконайтеся, що порт співпадає
    app.run(port=8000)