from auth_app import app
from ..controllers.controller import allControllers
controller=allControllers()
from flask import request,jsonify
# from .scheduler import start_scheduler
# start_scheduler()
# @app.route('/home')
# #@token_required
# def home_page():
#     return controller.home()

# @app.route('/signup', methods=['POST'])
# def signup_page():
#     return controller.signup_func()

# @app.route('/login', methods=['POST'])
# def login_page():
#     return controller.login_user()
# @app.route('/upload', methods=['POST'])
# def upload_page():
#     return controller.upload_img()
################# Mongo Engine #################
@app.route('/add_user', methods=['POST'])
def add_user_route():
    data = request.get_json()
    if data:
        new_user = controller.add_user(data)
        if new_user:
            # Handle success scenario
            return jsonify({'message': 'User added successfully'})
        else:
            # Handle the case where data is incomplete
            return jsonify({'error': 'Invalid data provided'}), 400
    else:
        return jsonify({'error': 'No data provided'}), 400
@app.route('/allUser', methods=['GET'])
def show_all_users():
    all_users = controller.show()
    return  (all_users)