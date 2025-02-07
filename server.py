from flask import Flask,render_template,url_for,request
import sqlite3
from waitress import serve
app = Flask(__name__)


# this will be removed and  replaced with the real backend code of the project at a later date

@app.route("/profile")
def EJ_profile():
    my_name_jason = {
        "name":"Elijah Quinones",
        "about":"I am a software engineer fellow at Hack.Diversity"
    }
    return my_name_jason


@app.route("/", methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        #connect to db
        connection = sqlite3.connect('Login.db')
        cursor = connection.cursor()

        username = request.form['username']
        password = request.form['password']

        # the '"+username+"' is using the actual varibale value instead of the String literal username
        check = "SELECT username,password FROM users where username='"+username+"'and password='"+password+"'"
        
        # checks the database for the username and password given
        cursor.execute(check)

        validate = cursor.fetchall()

        if len(validate) == 0:
            return render_template("login_unsucessfull.html")
        else:
            return render_template("dashboard.html")
        
    elif request.method == 'GET':
        return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port= 50100, threads =2)