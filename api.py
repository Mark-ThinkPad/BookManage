from flask import Blueprint, request
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from models import TBReader, TBReaderType, TBBook, TBBorrow, db_session

api = Blueprint('api', __name__)


@api.route('/user/login', methods=['POST'])
def login():
    uid = request.form.get('uid', False)
    pwd = request.form.get('pwd', False)
    if not (uid and pwd):
        return {'status': 0, 'message': '未输入用户ID或密码'}
    try:
        r: TBReader = TBReader.query.filter(TBReader.rdID == uid, TBReader.rdPwd == pwd).one()
        return {'status': 1, 'message': '登录成功',
                'uid': r.rdID, 'pwd': pwd, 'username': r.rdName}
    except NoResultFound:
        return {'status': 0, 'message': '用户ID或密码错误'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '用户数据异常'}


@api.route('/user/changePwd', methods=['POST'])
def changePwd():
    uid = request.form.get('uid', False)
    old_pwd = request.form.get('old_pwd', False)
    new_pwd = request.form.get('new_pwd', False)
    if not (uid and old_pwd and new_pwd):
        return {'status': 0, 'message': '传入数据不完整'}
    try:
        session = db_session()
        r: TBReader = session.query(TBReader).filter(TBReader.rdID == uid, TBReader.rdPwd == old_pwd).one()
        r.rdPwd = new_pwd
        session.commit()
        session.close()
    except NoResultFound:
        return {'status': 0, 'message': '旧密码错误'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '用户数据异常'}
    else:
        return {'status': 1, 'message': '密码修改成功, 请重新登录'}


@api.route('/reader/type/add', methods=['POST'])
def addReaderType():
    pass


@api.route('/reader/type/find', methods=['POST'])
def findReaderType():
    pass


@api.route('/reader/type/change', methods=['POST'])
def changeReaderType():
    pass


@api.route('/reader/type/delete', methods=['POST'])
def deleteReaderType():
    pass
