from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name
         #"hola, me llamo ${nombre}"
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.name,
         }


class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Planet %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.name,
         }


class Fav_People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.String(120), db.ForeignKey("people.id"))
    email = db.Column(db.String(120), db.ForeignKey("user.email"))
    rel_people = db.relationship("People")
    rel_user = db.relationship("User")

    def __repr__(self):
        return '<Fav_people %r>' % self.email
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "people_name": self.people_name,
         }

class Fav_Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.String(120), db.ForeignKey("planet.id"))
    email = db.Column(db.String(120), db.ForeignKey("user.email"))
    rel_planet = db.relationship("Planet")
    rel_user = db.relationship("User")

    def __repr__(self):
        return '<Fav_planet %r>' % self.email
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "planet_name": self.planet_name,
         }