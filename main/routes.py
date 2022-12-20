from main import app
from flask import render_template, request, redirect, url_for, session
import sqlite3
from flask_session import Session


@app.route("/")
@app.route("/home")
def home():
    if not session.get("username"):
        return redirect("/login")
    db = sqlite3.connect("USERS.db")
    curr = db.cursor()
    query = f'select id,name,mobile from USERS where id ="{session.get("username")}"'
    curr.execute(query)
    x = curr.fetchone()
    curr.close()
    db.close()
    return render_template("dashboard.html", name=x[1], username=x[0], phone=x[2])


@app.route("/login", methods=["GET", "POST"])
# -----------------------------------user ------------------------------------------
def login():

    # return render_template("homepage.html")
    error = None
    if request.method == "POST":
        User = request.form["username"]
        Pass = request.form["password"]
        # query='select id,password from USERS where id ="%s%User"'
        db = sqlite3.connect("USERS.db")
        curr = db.cursor()
        query = f'select id,password from USERS where id ="{User}"'
        curr.execute(query)
        # Check the login credentials
        x = curr.fetchone()
        curr.close()
        db.close()

        if x:
            if User != x[0] or Pass != x[1]:
                error = "Invalid username or password. Please try again."

            else:
                session["username"] = request.form["username"]
                session["password"] = request.form["password"]
                # Login successful, redirect to the dashboard
                return redirect(url_for("home"))
        else:
            error = "Invalid username or password. Please try again."

    return render_template("login.html", error=error)


# --------------------------------sign up ------------------------------------
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
        db = sqlite3.connect("USERS.db")
        curr = db.cursor()
        # query="insert into users(id,name,password,mobile) values "
        curr.execute(
            f'insert into users(id,name,password,mobile) values("{session["username"]}","{session["name"]}","{session["password"]}","{session["phone"]}")'
        )
        db.commit()
        curr.close()
        db.close()
        return redirect(url_for("home"))
    return render_template("signup.html", error=error)


# -----------------------------------line----------------------------------------
@app.route("/logout")
def logout():
    session["username"] = None
    return redirect("/")


@app.route("/table")
def table():
    db = sqlite3.connect("USERS.db")
    curr = db.cursor()
    curr.execute("select * from users")
    result = curr.fetchall()
    return render_template("table.html", items=result)


@app.route("/lost")
def lost():
    db = sqlite3.connect("USERS.db")
    curr = db.cursor()
    curr.execute("select * from details where status='lost'")
    result = curr.fetchall()
    return render_template("items.html", items=result, type='Lost')


@app.route("/found")
def found():
    db = sqlite3.connect("USERS.db")
    curr = db.cursor()
    curr.execute("select * from details where status='found'")
    result = curr.fetchall()
    return render_template("found.html", items=result, type='Found')


@app.route("/report", methods=["GET", "POST"])
def report():
    msg = None
    if request.method == "POST":
        db = sqlite3.connect("USERS.db")
        curr = db.cursor()
        xyz = f'insert into details(name,id,item,desc,location,mobile,room,date,status) values("{request.form["name"]}","{request.form["username"]}","{request.form["iName"]}","{request.form["desc"]}","{request.form["location"]}","{request.form["phone"]}","{request.form["room"]}","{request.form["date"]}","{request.form["status"]}")'
        curr.execute(xyz)
        db.commit()
        curr.close()
        db.close()
        msg = "Report submitted successfully"
    return render_template("report.html", msg=msg)


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run()
