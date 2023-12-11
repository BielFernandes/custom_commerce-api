from flask import Flask
from config.Config import config #DB CONFIG
from src.models.base_model import * #BASE MODEL


app = Flask(__name__)
app.config.from_object(config) #DB CONFIG

db.init_app(app) #BASE MODEL
with app.app_context(): #CREATE BASE MODEL CHILDRENS
    db.create_all()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)