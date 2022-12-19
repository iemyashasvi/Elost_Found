from main import app
from flask import render_template,request,redirect,url_for
import sqlite3
@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
    db=sqlite3.connect("USERS.db")
    curr=db.cursor()

    #return render_template("homepage.html")
    error = None
    if request.method == 'POST':
        User=request.form['username']
        Pass=request.form['password']
        # Check the login credentials
        if User!= "admin" or Pass!= "password":
            error = 'Invalid username or password. Please try again.'

        else:
            # Login successful, redirect to the dashboard
            return redirect(url_for('dashboard'))
    return render_template('login1.html', error=error)

@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'

if __name__ == '__main__':
   app.run()