toConv = [1,3,4,9,12]
def main():
 
    # Make the input an integer
  key = int(input("What is the key value or the shift? "))
  
  toConv = [x + key for x in toConv]
  print("This is toConv", toConv)
main()

