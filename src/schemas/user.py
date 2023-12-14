from marshmallow import Schema, fields, post_load

class UserSchema(Schema):
    fname = fields.Str()
    lname = fields.Str()
    email = fields.Str()
    password = fields.Str()
    admin = fields.Bool()
    created_at = fields.Date()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)