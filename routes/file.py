import json
from io import BytesIO

import requests
from flask import Blueprint, Response, request, send_file
from flask_jwt_extended import jwt_required
from config import APIPaths

file_routes = Blueprint('file', __name__)


@file_routes.route('/<int:id_file>', methods=['GET'])
@jwt_required()
def get_tasks(id_file: int):
    type = request.args.get('type', None)
    if type is not None:
        uri = "{}{}{}?type={}".format(APIPaths.FILE_HOST, APIPaths.FILE_QUERY_PATH, id_file, type)
        response: Response = requests.get(uri, headers={"Authorization": "{}".format(request.headers.get('Authorization'))})
        if response.status_code != 200:
            return {
                "code": "fail",
                "msg": "failed during search file, please contact with support"
            }, response.status_code
        filename = response.headers['Content-Disposition'].split("=")[1]
        return send_file(BytesIO(response.content), download_name=filename)

    return {"fail": "type required"}, 400
