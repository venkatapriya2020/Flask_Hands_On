import os

from flask import Flask,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker
from decouple import config

app = Flask(__name__)

engine=create_engine(config('DB_URL'))
db=scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights=db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html",flights=flights)
    
@app.route("/book",methods=["POST"])
def book():
    """BOOK A FLIGHT"""
    
    name=request.form.get("name")
    try:
        flight_id=int(request.form.get("flight_id"))    
        print(flight_id)
    except ValueError:
        return render_template("error.html",message="Invalid Flight Number")
        
    if db.execute("SELECT * FROM flights WHERE id=:id",{"id":flight_id}).rowcount==0: 
       return render_template("error.html",message="No such flight with that id") 
       
    db.execute("INSERT INTO passengers (flight_id,name) VALUES(:flight_id,:name)",
            {"flight_id":flight_id,"name":name})
    db.commit()
    return render_template("success.html")     
    