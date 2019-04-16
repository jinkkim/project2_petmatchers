#import os
#import pandas as pd
#import numpy as np
#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine
#from flask_sqlalchemy import SQLAlchemy

from flask_pymongo import PyMongo
from flask import Flask, render_template
from bson.json_util import dumps

app = Flask(__name__)

# Database Setup
#app.config["MONGO_URI"] = "mongodb://localhost:27017/pets"
app.config["MONGO_URI"] = "mongodb+srv://k9sam:1234@petfinder-qbryn.mongodb.net/pets"

mongo = PyMongo(app)

# variables for collections in the "pets" DB
db_dogData = mongo.db.dogs_by_page
db_catData = mongo.db.cats_by_page
db_cost = mongo.db.annual_costs


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/adoptadog")
def adoptadog():
    animals = list(db_dogData.find().limit(100))
    return render_template("adoptadog.html", animals = animals)


@app.route("/adoptacat")
def adoptacat():
    animals = list(db_catData.find().limit(100))
    return render_template("adoptacat.html", animals = animals)

@app.route("/cost")
def cost():
    cost_data = dumps(db_cost.find())
    return render_template("cost.html", cost_data = cost_data)

    
@app.route("/aboutdogs")
def about_dog():

    return render_template("aboutdogs.html")

@app.route("/aboutcats")
def about_cat():
    return render_template("aboutcats.html")



if __name__ == "__main__":
    app.run()