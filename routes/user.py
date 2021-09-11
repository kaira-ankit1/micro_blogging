from flask import Blueprint,request,jsonify
from service.user import User
from . import routes

@routes.route("/register", methods=["POST"])
def register():
    formData = request.json
    errors = []
    if ('firstName' not in formData) or (formData['firstName'] is None):
        errors.append("Please provide First Name")
    if ('lastName' not in formData) or (formData['lastName'] is None):
        errors.append("Please provide Last Name")
    if ('emailId' not in formData) or (formData['emailId'] is None):
        errors.append("Please provide Email Id")
    if ('username' not in formData) or (formData['username'] is None):
        errors.append("Please provide Username")
    if ('password' not in formData) or (formData['password'] is None):
        errors.append("Please provide Password")
    if ('dateOfBirth' not in formData) or (formData['dateOfBirth'] is None):
        errors.append("Please provide Date of Birth")
    if len(errors) > 0 :
        return jsonify({"status":"error","error":errors})
    else:
        return User.register(formData)


@routes.route("/login", methods=["POST"])
def login():
    formData = request.json
    errors = []
    if ('username' not in formData) or (formData['username'] is None):
        errors.append("Please provide First Name")
    if ('password' not in formData) or (formData['password'] is None):
        errors.append("Please provide Password")
    if len(errors) > 0 :
        return jsonify({"status":"error","error":errors})
    else:
        return User.login(formData)