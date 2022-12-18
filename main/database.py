import sqlite3
db=sqlite3.connect("USERS.db")
curr=db.cursor()
curr.execute("select ID, password from users")
x=curr.fetchone()
print(x[0],x[1])