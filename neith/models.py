from neith import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(24), unique=True, nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    user_image = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.user_image}')"
