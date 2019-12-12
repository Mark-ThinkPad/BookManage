from flask import Blueprint, render_template

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/user/login')
def user_login():
    return render_template('login.html')


@views.route('/user/changePwd')
def change_pwd():
    return render_template('changePwd.html')
