flock = [5,7,300,90,24,50,75]
print("Hello, my name is Tuyen and these are my ship size")
print("[ ",end="")
print(*flock,sep=", ",end="")
print(" ]")

print("Now my biggest sheep has size",max(flock)," let's share it")
n = flock.index(max(flock))
flock[n] = 8
print("After sharing, here is my flock")
print(*flock,sep=", ")

print("MONTH 1:","/n","One month has  passed, now here is my flock")
flock =[x+50 for x in flock]
print(*flock,sep=", ")
print("Now my biggest sheep has size",max(flock)," let's share it")
n = flock.index(max(flock))
flock[n] = 8
print("After sharing, here is my flock")
print(*flock,sep=", ")

print("MONTH 2:","/n","One month has  passed, now here is my flock")
flock =[x+50 for x in flock]
print(*flock,sep=", ")
print("Now my biggest sheep has size",max(flock)," let's share it")
n = flock.index(max(flock))
flock[n] = 8
print("After sharing, here is my flock")
print(*flock,sep=", ")

print("MONTH 3:","/n","One month has  passed, now here is my flock")
flock =[x+50 for x in flock]
print(*flock,sep=", ")
print("My flock has size in total: ",sum(flock))
print("I would get",sum(flock),"* 2$ = ",2*sum(flock)," $")

