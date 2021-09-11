import hashlib
from flask import jsonify
from db.connection import Connection
from utils.util import getRandomString 
class User:
    def register(formData):
        password = formData['password']
        salt = getRandomString()
        passwordToEncypt = (password+salt).encode("utf-8")		
        enceyptedPassword = hashlib.md5(passwordToEncypt).hexdigest()
        conn = Connection.getConnection()
        mycursor = conn.cursor()
        sql = "INSERT INTO user (first_name, last_name, email_id, username, password, salt, date_of_birth) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (formData['firstName'], formData['lastName'], formData['emailId'],formData['username'],enceyptedPassword,salt,formData['dateOfBirth'])
        mycursor.execute(sql, val)
        conn.commit()
        return jsonify({"status":"success","Username":formData['username']})

    def login(formData):
        username = formData['username']
        conn = Connection.getConnection()
        mycursor = conn.cursor()
        saltSearch = "select * from user where username = %s"
        print(username)
        mycursor.execute(saltSearch, (username))
        salt = mycursor.fetchall()
        print(salt)
        return "Hii"