from poll import Poll
from random import choice
import string
import mlab

#1. Connect to database
mlab.connect()

#2. Prepare data
q = "Hackathon an gi ?"
opts = [
    "Pizza",
    "Banh my Hoi An",
    "Pho xao",
]
alphabet = "abcdefghijklmnoprstuvwxyz".upper()

c =""
for _ in range(6):
    c += choice(alphabet)
print(c)
# #3. Create document
# p = Poll(question=q,options=opts,code=c)

# #4. Save
# p.save()


