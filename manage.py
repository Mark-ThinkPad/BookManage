from flask import Flask
from api import api
from views import views
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.register_blueprint(views)
app.register_blueprint(api, url_prefix='/api')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://LibAdmin:qwert123.@127.0.0.1:1433/Library'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run(debug=True)
