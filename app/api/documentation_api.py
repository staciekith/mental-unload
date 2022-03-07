from flask import Blueprint
from flask import jsonify
from flask_swagger import swagger
from flask import current_app
from flask import render_template

documentation_api = Blueprint('documentation_api', __name__)

@documentation_api.route('/swagger_json')
def get_swagger_json():
    return jsonify(swagger(current_app))

@documentation_api.route('/')
def get_documentation():
    return render_template('swaggerui.html')