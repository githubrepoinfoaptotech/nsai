from model.User import User
from utils.passwordEncryption import encrypt_password, compare_passwords
from utils.JwtToken import generate_token

from flask import jsonify, make_response,Flask, render_template, request,session
import os
import datetime
import random
import string
from database import db

def register(data):
    try:
        # Find Operation
        user = User.query.filter_by(email=data['email']).first()
        if user:
            return make_response({'message': "User Already Exist","status":True}, 200)
        else:
        # Add Operation
            new_user = User(username=data['username'], email=data['email'], password=encrypt_password(data['password']))
            db.session.add(new_user)
            db.session.commit()
            return make_response({'message': "User Added Successfully","status":True}, 200)
    except Exception as e:
        return make_response({'message': str(e)}, 404) 
    

def login(data):
    try:
        user = User.query.filter_by(email=data['email']).first()
        #print(user.email)
        if user:
            payload = {"email": user.email, "user_id": str(user.id),"name":user.username}
            if compare_passwords(str(data['password']), str(user.password)):
                secret = os.environ.get('TOKEN_SECRET')
                token = generate_token(payload, secret)
                return make_response({'token': token,"status":True}, 200)
            else:
                return make_response({'message': 'Invalid password',"status":False}, 403)      
        else:
        # Add Operation
            return make_response({'message': "User Not Found","status":False}, 200)   
    except Exception as e:
        return make_response({'message': str(e)}, 404) 
    



#  secret = os.environ.get('TOKEN_SECRET')
#         token = generate_token(payload, secret)