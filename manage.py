from flask import Flask
from api import api
from views import views

app = Flask(__name__)
app.register_blueprint(views)
app.register_blueprint(api, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True)
