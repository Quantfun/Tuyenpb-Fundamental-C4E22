from poll import Poll
import mlab

#1.
mlab.connect()

#2. Read all
poll_list = Poll.objects() #page, lazy loading
for p in poll_list:
    print(p.question)
    print(p.options)
    print(p.code)



