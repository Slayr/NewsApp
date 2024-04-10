# -*- coding: utf-8 -*-
"""Untitled14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11HKY1TUohgM66d--ZiAJzVYDLEB0Bsgb
"""

from init import app, jsonify, bcrypt
from auth import *
from Appdb import User, News


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

@app.route('/login')
def login():
    id = request.headers.get('User_id')
    password = request.headers.get("pass")
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    x = User.query.filter_by(id=id).first();





@app.route('/')
def index_view():
    return jsonify(msg="hello world")


if __name__ == "__main__":
    app.run(debug=True)