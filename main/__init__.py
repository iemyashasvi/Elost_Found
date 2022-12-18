from flask import Flask,render_template,request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
app=Flask(__name__,template_folder="templates")#URI:UNIFORM RESOURCE IDENTIFIER
app.config ['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'  #DICTIONARY THAT ACCEPTS KEY VALUE
db=SQLAlchemy(app)
from main import routes