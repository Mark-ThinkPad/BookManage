from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/', methods=['POST'])
def one():
    return {'api': 'response'}
