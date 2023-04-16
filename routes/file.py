import json
import requests
from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required
from config import APIPaths

file_routes = Blueprint('file', __name__)


@file_routes.route('/<int:id_file>', methods=['GET'])
@jwt_required()
def get_tasks(id_file: int):
    uri = "{}{}{}".format(APIPaths.TASK_HOST, APIPaths.TASK_SINGLE_QUERY_PATH, id_file)
    response: Response = requests.get(uri, headers={"Authorization": "{}".format(request.headers.get('Authorization'))})

    response_body = json.loads(response.text)
    if response.status_code != 200:
        return {
            "code": "fail",
        }, response.status_code

    return {}
