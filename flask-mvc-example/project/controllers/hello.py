from project import app
from flask import render_template, request, redirect, url_for
from project.models.User import findUserByUsername
from project.models.endpoints import *

#route index

#på rot gjør den dette
@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "POST":
        
        username = request.form["username"]
        try:
            user = findUserByUsername(username)
            #denne funksjonen returnerer et User-objekt med enten data fra databasen, eller en melding om at det ikke finnes noe som passer
            data = {
                "username": user.username,
                "email": user.email
            }
        except Exception as err:
            print (err)
#Dette er bare det som kommer opp før du har skrevet noe
    else:
        data = {
            "username": "Not specified",
            "email": "Not specified"
        }
    return render_template('index.html.j2', data = data)

