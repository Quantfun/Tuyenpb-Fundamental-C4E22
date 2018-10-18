#Write a function that removes the dollar sign (“$”) in a string, named remove_dollar_sign, takes 1 arguments: s, 
# where s is the input string, returns the new string with no dollar sign in it

def remove_dollar_sign(oldstring):
    newstring = oldstring.replace("$","")
    return newstring

# oldstring = "$" + input("input your saving money:")
# # newstring = oldstring.replace("$","")
# # print(newstring)

# remove_dollar_sign(oldstring)


