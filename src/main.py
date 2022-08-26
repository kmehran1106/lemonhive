from flask import Flask
from flask_marshmallow import Marshmallow
from dotenv import dotenv_values

from api.controllers import api_blueprint

config = dotenv_values(".env")

DEBUG = bool(int(config.get("DEBUG", "1")))
ENVIRONMENT = config.get("ENVIRONMENT", "DEVELOPMENT")

app = Flask(__name__)
ma = Marshmallow(app)

app.register_blueprint(api_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=DEBUG)
