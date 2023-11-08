from flask import  jsonify,request,json
# from ..db.config import mongo
# from datetime import datetime, timedelta
# from auth_app import bcrypt,app
# import jwt
# import mongoengine
# from functools import wraps

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         Bereartoken = request.headers.get('Authorization')
#         token= Bereartoken.split(' ')[1]

#         if not token:
#             return jsonify({'message': 'Token is missing!'}), 401

#         try:
#             data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
#         except:
#             return jsonify({'message': 'Token is invalid!'}), 401

#         return f(*args, **kwargs)

#     return decorated
# hardcoded_data = {
#     'email': 'alikhant1@gmail.com',
#     'password': '12345678',
#     'name':"dummy"
# }
# class allControllers:
#  with app.app_context():

#     def home(self):
#          # Fetch the user object from MongoDB
#       users = list(mongo.db.Con.find())
#       for user in users:
#          if '_id' in user:
#             print(user['_id'])
#             user['_id'] = str(user['_id'])
#       print(users)
#     #   return jsonify(users)

#     def signup_func(self):
#         data =hardcoded_data # Get the JSON data sent in the POST request

#         if 'name' in data and 'email' in data and 'password' in data:
#             existing_user = mongo.db.Con.find_one({'email': data['email']})

#             if existing_user:
#                 print(f"message: 'User with this email already exists'")
#                 return({'message': 'User with this email already exists'}) #add the jsonify
#             # password hashing
#             cryptedPassword = bcrypt.generate_password_hash(data['password']).decode('utf8')
#             new_user = {
#                 'name': data['name'],
#                 'email': data['email'],
#                 'password': cryptedPassword,
#             }

#             # Insert the new user into the MongoDB collection
#             inserted_user = mongo.db.Con.insert_one(new_user)
#             new_user['_id'] = str(inserted_user.inserted_id)  # Convert ObjectId to string
#             print(new_user)
#             # return jsonify(new_user)
#         else:
#             print(f"'message': 'password and email are required for signup'")
#             # return jsonify({'message': 'password and email are required for signup'})
#     def login_user(self):
#         data = request.json

#         if 'email' in data and 'password' in data:
#             existing_user = mongo.db.Con.find_one({'email': data['email']})

#             if existing_user:
#                 password_hash = existing_user.get('password')
#                 if bcrypt.check_password_hash(password_hash, data['password']):
#                     try:
#                         expiration_time = datetime.utcnow() + timedelta(minutes=5)
#                         token = jwt.encode(
#                             {'email': data['email'], 'exp': expiration_time},  # Add 'exp' key with expiration time
#                             app.config['SECRET_KEY'],
#                             algorithm='HS256')
#                         return jsonify({
#                             "message": "Successfully logged in",
#                             "token":f"bearer {token}"
#                         })
#                     except Exception as e:
#                         return jsonify({
#                             "error": "Something went wrong",
#                             "message": str(e)
#                         }), 500
#                 else:
#                     return jsonify("Invalid email or password")
#             else:
#                 return jsonify("User does not exist")
#         else:
#             return jsonify({'message': 'Valid email and password are required for login'})
#     def upload_img(self):
#         if 'file' not in request.files:
#             return "No file part in the request", 400

#         file = request.files['file']
#         if file.filename == '':
#             return "No selected file", 400

#         if file:
#             file.save('auth_app/uploads/' + file.filename) 
#             return "File uploaded successfully", 200

#         return "File upload failed", 500
# class User(Document):
#     name = mongoengine.StringField()
#     age = mongoengine.IntField()

# ############for Mongo Engine #########
from ..models.user import User
class allControllers:
    def add_user(self, data):
            name = data.get('name')
            age = data.get('age')
            if name and age:
                new_user = User(name=name, age=age)
                new_user.save()
                return new_user
    def show(self):
        all_users = User.objects().to_json()
        return  jsonify(all_users)


