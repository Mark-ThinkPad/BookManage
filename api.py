from flask import Blueprint, request
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from models import TBReader, TBReaderType, TBBook, TBBorrow

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
                'uid': r.rdID, 'pwd': pwd, 'username': r.rdName,
                'role': r.rdAdminRoles}
    except NoResultFound:
        return {'status': 0, 'message': '用户ID或密码错误'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '用户数据异常'}
