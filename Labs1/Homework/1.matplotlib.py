from matplotlib import pyplot
machine_counts = [18,4,2]
machine_names = ["Pc", "Mac", "Linux"]

pyplot.pie(machine_counts, labels = machine_names, autopct="%f%%", shadow=True, explode =[0,0.2,0])
pyplot.axis("equal")
pyplot.show()