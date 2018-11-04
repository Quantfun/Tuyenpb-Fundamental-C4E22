import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds249233.mlab.com:49233/c4e22-poll

host = "ds249233.mlab.com"
port = 49233
db_name = "c4e22-poll"
user_name = "admin"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())