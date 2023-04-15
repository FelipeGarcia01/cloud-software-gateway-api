from flask_cors import  CORS
from flask import Flask
from flask_jwt_extended import JWTManager

from config import ProductionConfig
from routes.auth import auth_routes
from routes.file import file_routes
from routes.task import task_routes

app = Flask(__name__)
app.config.from_object(ProductionConfig)
app_context = app.app_context()
app_context.push()


cors = CORS(app)
jwt = JWTManager(app)

app.register_blueprint(auth_routes, url_prefix='/api/auth/')
app.register_blueprint(task_routes, url_prefix='/api/tasks/')
app.register_blueprint(file_routes, url_prefix='/api/files/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)