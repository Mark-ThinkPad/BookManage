from flask import Blueprint, render_template
from decorators import login_required, permission_check

views = Blueprint('views', __name__)


@views.route('/')
def index():
    return render_template('index.html')


@views.route('/user/login')
def user_login():
    return render_template('login.html')


@views.route('/user/changePwd')
@login_required
def change_pwd():
    return render_template('changePwd.html')


@views.route('/reader/add')
@login_required
@permission_check(0b0001, True)
def add_reader():
    return render_template('addReader.html')


@views.route('/reader/type/manage')
@login_required
@permission_check(0b0001, True)
def readerTypeManage():
    return render_template('ReaderTypeManage.html')


@views.route('/404')
def error_404():
    return render_template('404.html'), 404


@views.route('/403')
def error_403():
    return render_template('403.html'), 403


@views.route('/500')
def error_500():
    return render_template('500.html'), 500
