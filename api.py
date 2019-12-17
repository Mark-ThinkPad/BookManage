from flask import Blueprint, request
from decorators import login_required, permission_check
from sqlalchemy.exc import OperationalError, IntegrityError
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from models import TBReader, TBReaderType, TBBook, TBBorrow, db_session
import datetime

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
@login_required
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
@login_required
@permission_check(0b0001, True)
def addReaderType():
    rdType = request.form.get('rdType', False)
    rdTypeName = request.form.get('rdTypeName', False)
    CanLendQty = request.form.get('CanLendQty', False)
    CanLendDay = request.form.get('CanLendDay', False)
    CanContinueTimes = request.form.get('CanContinueTimes', False)
    PunishRate = request.form.get('PunishRate', False)
    DateValid = request.form.get('DateValid', False)

    if not (rdType and rdTypeName and CanLendQty and CanLendDay and CanContinueTimes and PunishRate and DateValid):
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        session = db_session()
        rt = TBReaderType(rdType=rdType, rdTypeName=rdTypeName, CanLendQty=CanLendQty, CanLendDay=CanLendDay,
                          CanContinueTimes=CanContinueTimes, PunishRate=PunishRate, DateValid=DateValid)
        session.add(rt)
        session.commit()
        session.close()
    except OperationalError:
        return {'status': 0, 'message': '输入的数据类型可能有误'}
    except IntegrityError:
        return {'status': 0, 'message': '读者类型编号或读者类型名重复'}
    else:
        return {'status': 1, 'message': '新的读者类型添加成功'}


@api.route('/reader/type/find', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def findReaderType():
    rdType = request.form.get('rdType', False)
    rdTypeName = request.form.get('rdTypeName', False)

    if rdType is False and rdTypeName is False:
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        if rdType and rdTypeName:
            rt: TBReaderType = TBReaderType.query.filter(TBReaderType.rdType == rdType,
                                                         TBReaderType.rdTypeName == rdTypeName).one()
        if rdType and rdTypeName is False:
            rt: TBReaderType = TBReaderType.query.filter(TBReaderType.rdType == rdType).one()

        if rdType is False and rdTypeName:
            rt: TBReaderType = TBReaderType.query.filter(TBReaderType.rdTypeName == rdTypeName).one()

        return {'status': 1, 'message': '已找到一个读者类型', 'rdType': rt.rdType,
                'rdTypeName': rt.rdTypeName, 'CanLendQty': rt.CanLendQty,
                'CanLendDay': rt.CanLendDay, 'CanContinueTimes': rt.CanContinueTimes,
                'PunishRate': rt.PunishRate, 'DateValid': rt.DateValid}
    except NoResultFound:
        return {'status': 0, 'message': '没有查询到相应的读者类型'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '读者类型数据异常'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据类型可能有误'}


@api.route('/reader/type/change', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def changeReaderType():
    rdType = request.form.get('rdType', False)
    rdTypeName = request.form.get('rdTypeName', False)
    CanLendQty = request.form.get('CanLendQty', False)
    CanLendDay = request.form.get('CanLendDay', False)
    CanContinueTimes = request.form.get('CanContinueTimes', False)
    PunishRate = request.form.get('PunishRate', False)
    DateValid = request.form.get('DateValid', False)

    if not (rdType and rdTypeName and CanLendQty and CanLendDay and CanContinueTimes and PunishRate and DateValid):
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        session = db_session()
        rt: TBReaderType = session.query(TBReaderType).filter(TBReaderType.rdType == rdType).one()
        rt.rdTypeName = rdTypeName
        rt.CanLendQty = CanLendQty
        rt.CanLendDay = CanLendDay
        rt.CanContinueTimes = CanContinueTimes
        rt.PunishRate = PunishRate
        rt.DateValid = DateValid
        session.commit()
        session.close()
    except NoResultFound:
        return {'status': 0, 'message': '未找到指定的读者类型'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '读者类型数据异常'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据类型可能有误'}
    else:
        return {'status': 1, 'message': '指定的读者类型修改成功'}


@api.route('/reader/type/delete', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def deleteReaderType():
    rdType = request.form.get('rdType', False)
    rdTypeName = request.form.get('rdTypeName', False)

    if rdType is False and rdTypeName is False:
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        session = db_session()

        if rdType and rdTypeName:
            rt: TBReaderType = session.query(TBReaderType).filter(TBReaderType.rdType == rdType,
                                                                  TBReaderType.rdTypeName == rdTypeName).one()
        if rdType and rdTypeName is False:
            rt: TBReaderType = session.query(TBReaderType).filter(TBReaderType.rdType == rdType).one()

        if rdType is False and rdTypeName:
            rt: TBReaderType = session.query(TBReaderType).filter(TBReaderType.rdTypeName == rdTypeName).one()

        session.delete(rt)
        session.commit()
        session.close()
    except NoResultFound:
        return {'status': 0, 'message': '未找到指定的读者类型'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '读者类型数据异常'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据类型可能有误'}
    else:
        return {'status': 1, 'message': '指定的读者类型删除成功'}


@api.route('/reader/add', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def addReader():
    rdID = request.form.get('rdID', False)
    rdName = request.form.get('rdName', False)
    rdSex = request.form.get('rdSex', False)
    rdType = request.form.get('rdType', False)
    rdDept = request.form.get('rdDept', False)
    rdPhone = request.form.get('rdPhone', False)
    rdEmail = request.form.get('rdEmail', False)

    if not (rdID and rdName and rdSex and rdType and rdDept and rdPhone and rdEmail):
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        session = db_session()
        r = TBReader(rdID=rdID, rdName=rdName, rdSex=rdSex, rdType=rdType,
                     rdDept=rdDept, rdPhone=rdPhone, rdEmail=rdEmail)
        session.add(r)
        session.commit()
        session.close()
    except IntegrityError:
        return {'status': 0, 'message': '已存在相同的借书证编号, 无法重新创建'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据可能有误'}
    else:
        return {'status': 1, 'message': '新借书证创建成功'}


@api.route('/reader/add/status', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def addReaderStatus():
    rdID = request.form.get('rdID', False)

    if rdID is False:
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        TBReader.query.filter(TBReader.rdID == rdID).one()
    except NoResultFound:
        return {'status': 1, 'message': '此人可以办理借书证'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '借书证数据异常'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据类型可能有误'}
    else:
        return {'status': 0, 'message': '该人已办理借书证, 无需再次办理'}


@api.route('/reader/change', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def changeReader():
    rdID = request.form.get('rdID', False)
    rdName = request.form.get('rdName', False)
    rdSex = request.form.get('rdSex', False)
    rdType = request.form.get('rdType', False)
    rdDept = request.form.get('rdDept', False)
    rdPhone = request.form.get('rdPhone', False)
    rdEmail = request.form.get('rdEmail', False)

    if not (rdID and rdName and rdSex and rdType and rdDept and rdPhone and rdEmail):
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        session = db_session()
        r: TBReader = session.query(TBReader).filter(TBReader.rdID == rdID).one()
        r.rdName = rdName
        r.rdSex = rdSex
        r.rdType = rdType
        r.rdDept = rdDept
        r.rdPhone = rdPhone
        r.rdEmail = rdEmail
        session.commit()
        session.close()
    except NoResultFound:
        return {'status': 0, 'message': '未找到指定的借书证'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '借书证数据异常'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据可能有误'}
    else:
        return {'status': 1, 'message': '指定的借书证修改成功'}


@api.route('/reader/loss/report', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def lossReport():
    rdID = request.form.get('rdID', False)

    if rdID is False:
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        session = db_session()
        r: TBReader = session.query(TBReader).filter(TBReader.rdID == rdID).one()
        if r.rdStatus == '有效':
            r.rdStatus = '挂失'
            session.commit()
            session.close()
            return {'status': 1, 'message': '挂失办理成功'}
        else:
            session.close()
            return {'status': 0, 'message': '该借书证状态不是有效, 无法办理挂失'}
    except NoResultFound:
        return {'status': 0, 'message': '未找到指定的借书证'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '借书证数据异常'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据可能有误'}


@api.route('/reader/loss/report/status', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def lossReportStatus():
    rdID = request.form.get('rdID', False)

    if rdID is False:
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        r: TBReader = TBReader.query.filter(TBReader.rdID == rdID).one()
        if r.rdStatus == '有效':
            return {'status': 1, 'message': '该借书证状态有效, 可以办理挂失'}
        else:
            return {'status': 0, 'message': '该借书证状态不是有效, 无法办理挂失'}
    except NoResultFound:
        return {'status': 0, 'message': '未找到指定的借书证'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '借书证数据异常'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据可能有误'}


@api.route('/reader/loss/cancel', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def lossCancel():
    rdID = request.form.get('rdID', False)

    if rdID is False:
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        session = db_session()
        r: TBReader = session.query(TBReader).filter(TBReader.rdID == rdID).one()
        if r.rdStatus == '挂失':
            r.rdStatus = '有效'
            session.commit()
            session.close()
            return {'status': 1, 'message': '解除挂失办理成功'}
        else:
            session.close()
            return {'status': 0, 'message': '该借书证状态不是挂失, 无法办理解除挂失'}
    except NoResultFound:
        return {'status': 0, 'message': '未找到指定的借书证'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '借书证数据异常'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据可能有误'}


@api.route('/reader/loss/cancel/status', methods=['POST'])
@login_required
@permission_check(0b0001, True)
def lossCancelStatus():
    rdID = request.form.get('rdID', False)

    if rdID is False:
        return {'status': 0, 'message': '传入数据不完整'}

    try:
        r: TBReader = TBReader.query.filter(TBReader.rdID == rdID).one()
        if r.rdStatus == '挂失':
            return {'status': 1, 'message': '该借书证状态为挂失, 可以办理解除挂失'}
        else:
            return {'status': 0, 'message': '该借书证状态不是挂失, 无法办理解除挂失'}
    except NoResultFound:
        return {'status': 0, 'message': '未找到指定的借书证'}
    except MultipleResultsFound:
        return {'status': 0, 'message': '借书证数据异常'}
    except OperationalError:
        return {'status': 0, 'message': '输入的数据可能有误'}
