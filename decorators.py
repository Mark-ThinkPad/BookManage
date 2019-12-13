from functools import wraps
from flask import request, redirect, url_for
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from models import TBReader


def login_required(f):
    @wraps(f)
    def isLogin(*args, **kwargs):
        uid = request.cookies.get('uid', False)
        pwd = request.cookies.get('pwd', False)
        if not (uid and pwd):
            return redirect(url_for('views.user_login'))
        try:
            TBReader.query.filter(TBReader.rdID == uid, TBReader.rdPwd == pwd).one()
        except NoResultFound:
            return redirect(url_for('views.user_login'))
        except MultipleResultsFound:
            return redirect(url_for('views.error_500'))
        else:
            return f(*args, **kwargs)
    return isLogin


def permission_check(role: bin, allowSysAdmin: bool = False):
    def authority(f):
        @wraps(f)
        def check(*args, **kwargs):
            uid = request.cookies.get('uid', False)
            pwd = request.cookies.get('pwd', False)
            r: TBReader = TBReader.query.filter(TBReader.rdID == uid, TBReader.rdPwd == pwd).one()
            user_role: int = r.rdAdminRoles
            if (user_role & role) == role:
                return f(*args, **kwargs)
            elif allowSysAdmin:
                if (user_role & 0b1000) == 0b1000:
                    return f(*args, **kwargs)
                else:
                    return redirect(url_for('views.error_403'))
            else:
                return redirect(url_for('views.error_403'))
        return check
    return authority
