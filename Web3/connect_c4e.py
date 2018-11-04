import mlab
from river import River

mlab.connect()

#Ex1. List all rivers in Africa
# river_list = River.objects(continent="Africa")

# for r in river_list:
#     print(r.name)


#Ex2. List all rivers in S. America & length <=1000
river_list = River.objects(continent="S. America", length_lte=1000)


for r in river_list:
    print(r.name)