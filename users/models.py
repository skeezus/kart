from extensions import bcrypt, db
import datetime


class User(db.Document):
    _id = db.ObjectIdField()
    # lots of duplicate mail fields
    # dupe query: https://stackoverflow.com/questions/14770170/how-to-find-mongo-documents-with-a-same-field
    name = db.StringField(max_length=100, required=True)
    email = db.EmailField(required=True)
    password = db.StringField(required=True)
    
    meta = {
        'collection': 'users'
    }

    def to_json(self):
        return {'id': str(self._id), 'name': self.name, 'email': self.email}

    #@staticmethod
    def encrypt_password(self, pass_raw):
        self.password = bcrypt.generate_password_hash(pass_raw).decode('utf-8')