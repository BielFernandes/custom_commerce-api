from marshmallow import Schema, fields, post_load
import bcrypt

class UserSchema(Schema):

    @staticmethod
    def hash_password(pwd):
        bytes = pwd.encode('utf-8') 
        salt = bcrypt.gensalt() 
        hash = bcrypt.hashpw(bytes, salt) 
        
        return hash


    fname = fields.Str()
    lname = fields.Str()
    email = fields.Str()
    password = fields.Str()
    admin = fields.Bool()
    created_at = fields.Date()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)