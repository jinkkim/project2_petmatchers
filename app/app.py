#import os
#import pandas as pd
#import numpy as np
#import sqlalchemy
#from sqlalchemy.ext.automap import automap_base
#from sqlalchemy.orm import Session
#from sqlalchemy import create_engine
#from flask_sqlalchemy import SQLAlchemy

from flask_pymongo import PyMongo
from flask import Flask, render_template, jsonify
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


def get_doge():
    dog_stats = {
        'breed': {},
        'age': {},
        'size': {},
        'gender': {},
        'color': {}
    }
    dogs = list(db_dogData.find().limit(100))
    for pupper in dogs:
        #print(pupper)
        if (pupper['breed']):
            #print('Breed:' + pupper['breed'])
            key = pupper['breed']
            #print(key)
            if key in dog_stats['breed']:
                dog_stats['breed'][key] += 1
            else:
                dog_stats['breed'][key] = 1
            #do the same for age
        if (pupper['age']):
            key = pupper['age']
            if key in dog_stats['age']:
                dog_stats['age'][key] += 1
            else:
                dog_stats['age'][key] = 1

        #do the same for size
        if (pupper['size']):
            key = pupper['size']
            if key in dog_stats['size']:
                dog_stats['size'][key] += 1
            else:
                dog_stats['size'][key] = 1

        #do the same for gender
        if (pupper['gender']):
            key = pupper['gender']
            if key in dog_stats['gender']:
                dog_stats['gender'][key] += 1
            else:
                dog_stats['gender'][key] = 1

    #do the same for color
        if (pupper['color']):
            key = pupper['color']
            if key in dog_stats['color']:
                dog_stats['color'][key] += 1
            else:
                dog_stats['color'][key] = 1
    return dog_stats

def get_kitteh():
    cat_facts = {
        'breed': {},
        'age': {},
        'size': {},
        'gender': {},
        'color': {}
    }
    kittehz = list(db_catData.find().limit(100))
    for kitteh in kittehz:
        #print(pupper)
        if (kitteh['breed']):
            #print('Breed:' + pupper['breed'])
            key = kitteh['breed']
            #print(key)
            if key in cat_facts['breed']:
                cat_facts['breed'][key] += 1
            else:
                cat_facts['breed'][key] = 1
            #do the same for age
        if (kitteh['age']):
            key = kitteh['age']
            if key in cat_facts['age']:
                cat_facts['age'][key] += 1
            else:
                cat_facts['age'][key] = 1

        #do the same for size
        if (kitteh['size']):
            key = kitteh['size']
            if key in cat_facts['size']:
                cat_facts['size'][key] += 1
            else:
                cat_facts['size'][key] = 1

        #do the same for gender
        if (kitteh['gender']):
            key = kitteh['gender']
            if key in cat_facts['gender']:
                cat_facts['gender'][key] += 1
            else:
                cat_facts['gender'][key] = 1

    #do the same for color
        if (kitteh['color']):
            key = kitteh['color']
            if key in cat_facts['color']:
                cat_facts['color'][key] += 1
            else:
                cat_facts['color'][key] = 1
    return cat_facts

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
    dog_stats = dumps(get_doge())
    return render_template("aboutdogs.html", dog_stats=dog_stats)
    #return jsonify(dog_stats)

@app.route("/aboutcats")
def about_cat():
    cat_facts = dumps(get_kitteh())
    return render_template("aboutcats.html", cat_facts=cat_facts)



if __name__ == "__main__":
    app.run()
