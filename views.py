from flask import Blueprint, render_template
from decorators import login_required, permission_check
from models import TBReaderType

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
    rts = TBReaderType.query.all()
    return render_template('addReader.html', rts=rts)


@views.route('/reader/change')
@login_required
@permission_check(0b0001, True)
def change_reader():
    rts = TBReaderType.query.all()
    return render_template('changeReader.html', rts=rts)


@views.route('/reader/loss/report')
@login_required
@permission_check(0b0001, True)
def loss_report():
    return render_template('lossReportReader.html')


@views.route('/reader/loss/cancel')
@login_required
@permission_check(0b0001, True)
def loss_cancel():
    return render_template('lossCancelReader.html')


@views.route('/reader/replace')
@login_required
@permission_check(0b0001, True)
def replace_Reader():
    return render_template('replaceReader.html')


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
