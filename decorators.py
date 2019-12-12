from functools import wraps
from flask import request, redirect, url_for, render_template
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