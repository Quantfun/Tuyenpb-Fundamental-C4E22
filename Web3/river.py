from mongoengine import Document, StringField, ListField, IntField

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()

