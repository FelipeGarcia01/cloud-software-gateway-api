import json

import requests
from flask import Blueprint, Response
from flask_jwt_extended import jwt_required, get_jwt_identity
from config import APIPaths

task_routes = Blueprint('tasks', __name__)


@task_routes.route('/<int:id_user>/tasks', methods=['GET'])
@jwt_required()
def get_tasks(id_user: int):

    if get_jwt_identity() != id_user:
        return {"error": "user does not have permissions"}, 503

    uri = APIPaths.TASK_HOST + APIPaths.TASK_LIST_PATH
    response: Response = requests.get(uri, headers={})
    response_body = json.loads(response.text)
    if response.status_code != 200:
        return {
                "code": "fail",
                "msg": response_body["error"]
            }, response.status_code

    return {}


@task_routes.route('/', methods=['POST'])
@jwt_required()
def create_task():
    uri = APIPaths.TASK_HOST + APIPaths.TASK_CREATE_PATH
    response: Response = requests.post(uri, json={}, headers={})
    response_body = json.loads(response.text)

    if response.status_code != 201:
        return {
            "code": "fail",
            "msg": response_body["error"]
        }, response.status_code

    return {}


@task_routes.route('/<int:id_user>/<int:id_task>', methods=['GET'])
@jwt_required()
def get_task(id_user: int, id_task: int):

    if get_jwt_identity() != id_user:
        return {"error": "user does not have permissions"}, 503

    uri = APIPaths.TASK_HOST + APIPaths.TASK_SINGLE_QUERY_PATH
    response: Response = requests.get(uri, headers={})
    response_body = json.loads(response.text)
    if response.status_code != 200:
        return {
            "code": "fail",
            "msg": response_body["error"]
        }, response.status_code

    return {}


@task_routes.route('/<int:id_task>', methods=['DELETE'])
@jwt_required()
def delete_task(id_task: int):
    uri = APIPaths.TASK_HOST + APIPaths.TASK_DELETE_PATH
    response: Response = requests.delete(uri, headers={})
    response_body = json.loads(response.text)

    if response.status_code != 204:
        return {
            "code": "fail",
            "msg": response_body["error"]
        }, response.status_code

    return {}