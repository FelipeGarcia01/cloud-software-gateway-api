import requests
from flask import Blueprint, Response, request, json
from flask_jwt_extended import jwt_required
from config import APIPaths

task_routes = Blueprint('tasks', __name__)


@task_routes.route('/', methods=['GET'])
@jwt_required()
def get_tasks():
    max = request.args.get('max', None)
    order = request.args.get('order', 0)

    uri ="{}{}?order={}".format(APIPaths.TASK_HOST, APIPaths.TASK_LIST_PATH, order) if max is None else "{}{}?order={}&max={}".format(APIPaths.TASK_HOST, APIPaths.TASK_LIST_PATH, order, max)

    response: Response = requests.get(uri, headers={'Content-Type': 'application/json', "Authorization": "{}".format(request.headers.get('Authorization'))})

    if response.status_code != 200:
        return {
                "code": "fail"
            }, response.status_code

    return json.loads(response.text)


@task_routes.route('/', methods=['POST'])
@jwt_required()
def create_task():
    uri = APIPaths.TASK_HOST + APIPaths.TASK_CREATE_PATH
    file = request.files['file']
    new_format = request.form.get('newFormat', None)
    data = {'newFormat': new_format}
    files = {'file': (file.filename, file.read())}

    response: Response = requests.post(uri, data=data, files=files, headers={"Authorization": "{}".format(request.headers.get('Authorization'))})

    if response.status_code != 201:
        return {
            "code": "fail"
        }, response.status_code

    return json.loads(response.text)


@task_routes.route('/<id_task>', methods=['GET'])
@jwt_required()
def get_task(id_task: str):
    uri = "{}{}{}".format(APIPaths.TASK_HOST, APIPaths.TASK_SINGLE_QUERY_PATH, id_task)

    response: Response = requests.get(uri, headers={"Authorization": "{}".format(request.headers.get('Authorization'))})

    if response.status_code != 200:
        return {
            "code": "fail"
        }, response.status_code

    return json.loads(response.text)


@task_routes.route('/<id_task>', methods=['DELETE'])
@jwt_required()
def delete_task(id_task: str):
    uri = "{}{}{}".format(APIPaths.TASK_HOST, APIPaths.TASK_SINGLE_QUERY_PATH, id_task)
    response: Response = requests.delete(uri, headers={"Authorization": "{}".format(request.headers.get('Authorization'))})
    response_body = json.loads(response.text)

    if response.status_code == 204:
        return {}, response.status_code

    return {"code": "fail", 'message': response_body["response"]}, response.status_code
