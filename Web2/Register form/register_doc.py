from mongoengine import Document, StringField, ListField, IntField

class  Register_doc(Document):
    first_name = StringField()
    last_name = StringField()
    email = StringField()
    yob = IntField()
    gender = StringField()
    city = StringField()
    code = StringField()

