from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 't1NP63m4wnBg6nyHYKmc2TpCORGI4nss'

api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost:27017/userDatabase'
}


initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
    app.run(debug=True)
