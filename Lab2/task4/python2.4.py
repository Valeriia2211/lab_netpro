from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def headers_processing():
    content_type = request.headers.get('Content-Type')
    data = {"currency": "USD", "rate": 41.5}

    if content_type == 'application/json':
        return jsonify(data)
    elif content_type == 'application/xml':
        return f"<currency><name>USD</name><rate>41.5</rate></currency>", 200, {'Content-Type': 'application/xml'}

    return "USD - 41,5 (joke = а колись був по 7...)"


if __name__ == '__main__':
    app.run(port=8000)