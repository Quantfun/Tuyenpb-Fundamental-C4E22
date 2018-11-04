# 1. Creat flask
# 2. Create html for form
# 3. Register form
# 4. Get form and process

from flask import Flask, render_template, request
import mlab
from random import choice
from register_doc import Register_doc

app = Flask(__name__)
mlab.connect()

@app.route("/")
def home():
    return render_template("home.html")

 
@app.route("/register",methods=["GET", "POST"])
def register():
        if request.method == "GET":
            return render_template("register.html")
        elif request.method == "POST":
            form = request.form
            first_name = form['First name']
            last_name = form['Last name']
            email = form['Email']
            yob = form['Yob']
            gender = form['Gender']
            city = form['City']
                        
            
        print(form)

        alphabet = "abcdefghijklmnoprstuvwxyz".upper()

        code =""
        for _ in range(6):
                code += choice(alphabet)
        
        r = Register_doc(first_name = first_name,last_name = last_name, email = email, yob = yob, gender = gender, city = city, code = code)
        r.save()   

        return "COOL !"    

if __name__ == '__main__':
    app.run(debug=True)

