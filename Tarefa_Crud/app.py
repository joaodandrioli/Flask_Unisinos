from flask import Flask
from models import db
from routes import init_routes
import os

app = Flask(__name__)

# Banco SQLite no diretório do projeto
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tasks.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
