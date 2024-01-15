from flask import (Flask, request)
from dotenv import load_dotenv 
import os
import bcrypt
import random

load_dotenv()

app = Flask(__name__)

@app.route("/")
def Home():
    return "Hello, World!"

@app.route("/EnrolStudent", methods=("GET", "POST"))
def enrol_Student():
    random_number = random.randint(1, 999)
    unique_id = f'CEE{random_number:03}'
    if request.methods == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        matricno = request.form['matricno']
        coursecode = request.form['coursecode']
        coursetitle = request.form['coursetitle']
        password = request.form['password']
    
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    



@app.route("/ExamLogin", methods=("GET", "POST"))
def exam_Login():
    if request.methods == "POST":
        matricno = request.form["matricno"]
        password = request.form["password"]
    
    
    
@app.get("/createAdmin")
def create_Admin():
    return    
    
if __name__ == "__main__":
    app.run(debug=True)