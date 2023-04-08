import json

import requests
from flask import Blueprint, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import APIPaths

file_routes = Blueprint('file', __name__)


@file_routes.route('/<int:id_user>/<int:id_file>', methods=['GET'])
@jwt_required()
def get_tasks(id_user: int, id_file: int):

    if get_jwt_identity() != id_user:
        return {"error": "user does not have permissions"}, 503

    uri = APIPaths.FILE_HOST + APIPaths.FILE_QUERY_PATH
    response: Response = requests.get(uri, headers={})
    response_body = json.loads(response.text)
    if response.status_code != 200:
        return {
            "code": "fail",
            "msg": response_body["error"]
        }, response.status_code

    return {}
