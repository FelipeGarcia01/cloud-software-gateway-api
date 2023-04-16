import json
import requests
from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import APIPaths

file_routes = Blueprint('file', __name__)


@file_routes.route('/<int:id_file>', methods=['GET'])
@jwt_required()
def get_tasks(id_file: int):

    uri = APIPaths.FILE_HOST + APIPaths.FILE_QUERY_PATH + str(id_file)
    response: Response = requests.get(uri, headers={})
    response_body = json.loads(response.text)
    if response.status_code != 200:
        return {
            "code": "fail",
            "msg": response_body["error"]
        }, response.status_code

    return {}
