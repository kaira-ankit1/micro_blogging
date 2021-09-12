import hashlib
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from flask_login import login_user
from model.user import User
from db.Connection import db

class AuthService:
    def register(formData):
        response = {"status" : "error"}
        email = formData.get('email')
        firstName = formData.get('firstName')
        lastName = formData.get('lastName')
        username = formData.get('username')
        password = formData.get('password')

        user = User.query.filter_by(username=username).first()
        
        if user:   
            response["message"] = "Email address already exists"
        else:
            new_user = User(email=email, firstName=firstName, lastName=lastName, username=username, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            response["status"] = "success"
            response["message"] = "user has been successfully"
        return jsonify(response)

    def login(formData):
        response = {"status" : "error"}
        username = formData.get('username')
        password = formData.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not check_password_hash(user.password, password): 
             response["message"] = "Please check your login details and try again."
        else:
            login_user(user)
            response["status"] = "success"
            response["message"] = "User logged in successfully"
        return jsonify(response)