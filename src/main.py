from flask import Flask
from flask_marshmallow import Marshmallow
from decouple import config

from api.controllers import api_blueprint

DEBUG = bool(int(config("DEBUG", default="1")))
ENVIRONMENT = config("ENVIRONMENT", default="DEVELOPMENT")

app = Flask(__name__)
ma = Marshmallow(app)

app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=DEBUG)
