import os

import pandas as pd
import numpy as np

from flask_pymongo import PyMongo
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


#################################################
# Database Setup
#################################################

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")

@app.route("/adoptadog")
def findDog():
    return render_template("findadog.html")

@app.route("/adoptacat")
def findCat():
    return render_template("findacat.html")
    
@app.route("/about")
def overview():
    return render_template("about.html")

@app.route("/maps")
def maps():
    return render_template("maps.html")

@app.route("/cost")
def cost():
    return render_template("cost.html")

if __name__ == "__main__":
    app.run()
