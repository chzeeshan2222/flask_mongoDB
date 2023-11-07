from flask import  jsonify,request
from ..db.config import mongo
from auth_app import bcrypt,app
import jwt
from functools import wraps
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        Bereartoken = request.headers.get('Authorization')
        token= Bereartoken.split(' ')[1]

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(*args, **kwargs)

    return decorated

class allControllers:
    def home(self):
         # Fetch the user object from MongoDB
      users = list(mongo.db.Con.find())
      for user in users:
         if '_id' in user:
            print(user['_id'])
            user['_id'] = str(user['_id'])
      return jsonify(users)

    def signup_func(self):
        data = request.json  # Get the JSON data sent in the POST request

        if 'name' in data and 'email' in data and 'password' in data:
            existing_user = mongo.db.Con.find_one({'email': data['email']})

            if existing_user:
                return jsonify({'message': 'User with this email already exists'})
            # password hashing
            cryptedPassword = bcrypt.generate_password_hash(data['password']).decode('utf8')
            new_user = {
                'name': data['name'],
                'email': data['email'],
                'password': cryptedPassword,
            }

            # Insert the new user into the MongoDB collection
            inserted_user = mongo.db.Con.insert_one(new_user)
            new_user['_id'] = str(inserted_user.inserted_id)  # Convert ObjectId to string

            return jsonify(new_user)
        else:
            return jsonify({'message': 'password and email are required for signup'})
    def login_user(self):
        data = request.json

        if 'email' in data and 'password' in data:
            existing_user = mongo.db.Con.find_one({'email': data['email']})

            if existing_user:
                password_hash = existing_user.get('password')
                if bcrypt.check_password_hash(password_hash, data['password']):
                    try:
                        token = jwt.encode({'email': data['email']},app.config['SECRET_KEY'], algorithm='HS256')
                        return jsonify({
                            "message": "Successfully logged in",
                            "token":f"bearer {token}"
                        })
                    except Exception as e:
                        return jsonify({
                            "error": "Something went wrong",
                            "message": str(e)
                        }), 500
                else:
                    return jsonify("Invalid email or password")
            else:
                return jsonify("User does not exist")
        else:
            return jsonify({'message': 'Valid email and password are required for login'})
