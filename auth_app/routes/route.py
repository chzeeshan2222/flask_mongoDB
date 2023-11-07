from auth_app import app
from ..controllers.controller import allControllers,token_required
controller=allControllers()

@app.route('/home')
@token_required
def home_page():
    return controller.home()

@app.route('/signup', methods=['POST'])
def signup_page():
    return controller.signup_func()

@app.route('/login', methods=['POST'])
def login_page():
    return controller.login_user()
