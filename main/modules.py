
class Items (db.Model):
    ID=db.Column(db.String(length=15),primary_key=True)
    name=db.Column(db.String(length=20),nullable=False)
    mobile=db.Column(db.String(length=20),nullable=False)
    item=db.Column(db.String(length=30),nullable=False)
    description=db.Column(db.String(length=1024),nullable=False)