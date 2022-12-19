from main import app
from flask import render_template,request,redirect,url_for,session
import sqlite3
from flask_session import Session
@app.route("/")
@app.route("/login",methods=['GET','POST'])
#-----------------------------------user ------------------------------------------
def login():
    
    #return render_template("homepage.html")
    error = None
    if request.method == 'POST':
        User=request.form['username']
        Pass=request.form['password']
        # query='select id,password from USERS where id ="%s%User"'
        db=sqlite3.connect("USERS.db")
        curr=db.cursor()
        query=f'select id,password from USERS where id ="{User}"'
        curr.execute (query)
        # Check the login credentials
        x=curr.fetchone()
        curr.close()
        db.close()

        if x:
            if User!= x[0] or Pass!= x[1]:
                error = 'Invalid username or password. Please try again.'

            else:
            # Login successful, redirect to the dashboard
                return redirect(url_for('dashboard'))
        else:
            error = 'Invalid username or password. Please try again.'

    return render_template('login.html', error=error)
@app.route("/signup", methods=["GET", "POST"])
def signup():
    error = None
    if request.method == "POST":
        # if already exist don't allow need to change the below
        # if request.form["username"] != "admin" or request.form["password"] != "admin":
        #     error = "User already exists."
        # else:
            session["username"] = request.form["username"]
            session["name"] = request.form["name"]
            session["password"] = request.form["password"]
            session["phone"] = request.form["phone"]
            db=sqlite3.connect("USERS.db")
            curr=db.cursor()
            #query="insert into users(id,name,password,mobile) values "
            curr.execute(f'insert into users(id,name,password,mobile) values({session["username"]},{session["name"]},{session["password"]},{session["phone"]})')
            db.commit()
            return redirect(url_for("home"))
    return render_template("signup.html", error=error)


@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")


@app.route('/dashboard')
def dashboard():
    return 'Welcome to the dashboard!'

if __name__ == '__main__':
   app.run()