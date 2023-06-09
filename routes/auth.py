import json

import requests
from flask import Blueprint, request, Response
from dtos.UserSignUpDTO import UserSignUpDTO, UserLogInDTO
from config import APIPaths

auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/signup', methods=['POST'])
def signup():
    try:
        request_data: UserSignUpDTO = json.loads(request.data, object_hook=UserSignUpDTO.from_json)
        uri = APIPaths.USER_HOST+APIPaths.SIGNUP_PATH
        data = {
            "username": request_data.user,
            "password1": request_data.password1,
            "password2": request_data.password2,
            "email": request_data.email
        }
        response: Response = requests.post(uri, json=data, headers= {"Content-Type": "application/json"})
        response_body = json.loads(response.text)

        if response.status_code == 201:
            return {
                "code": "created"
            }, 201
        else:
            return {
                "code": "fail",
                "msg": response_body["error"]
            }, response.status_code

    except KeyError:
        return {"error": "Bad request"}, 400
    except:
        return {"error": "internal error please try again"}, 500


@auth_routes.route('/login', methods=['POST'])
def signin():
    try:
        request_data: UserLogInDTO = json.loads(request.data, object_hook=UserLogInDTO.from_json)
        uri = APIPaths.USER_HOST+APIPaths.SIGNIN_PATH
        data = {
            "username": request_data.user,
            "password": request_data.password
        }
        response: Response = requests.post(uri, json=data, headers={"Content-Type":"application/json"})
        response_body = json.loads(response.text)
        if response.status_code == 200:
            return {
                "code": "success",
                "token": response_body["token"],
                "user": response_body["id"]
            }, 200
        else:
            return {
                "code": "fail",
                "msg": response_body["error"]
            }, response.status_code

    except KeyError:
        return {"error": "Bad request"}, 400
    except:
        return {"error": "internal error please try again"}, 500
