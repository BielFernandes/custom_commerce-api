from flask import Flask
from config.Config import config #DB CONFIG


app = Flask(__name__)
app.config.from_object(config) #DB CONFIG


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)