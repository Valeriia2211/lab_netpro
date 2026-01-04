from flask import Flask, request

app = Flask(__name__)


@app.route("/save", methods=['POST'])
def save_to_file():
    # Отримуємо текст із тіла запиту
    text_data = request.data.decode('utf-8')

    # Записуємо у файл (режим 'a' додає нові рядки в кінець)
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(text_data + "\n")

    return f"Успішно збережено: {text_data}"


if __name__ == '__main__':
    app.run(port=8000)