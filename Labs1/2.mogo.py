from pymongo import MongoClient
uri = "mongodb://Quant1:PBT12345@ds125273.mlab.com:25273/quantfun"


# #Connect to database
client = MongoClient(uri)
db = client.get_default_database()

# #Collection
posts = db["posts"]

post_list = posts.find() #insert_one(C), find(R)
for p in post_list:

    print(p['author'])
    print(p['title'])
    print(p['content'])

# #Document

# #Create a document
# post = {
#     "title": "Hom nay troi dep",
#     "content": "Toi di choi vong quanh the gioi",
#     "author": "PBT"
# }

# posts.insert_one(post)


# #Insert created document to database



