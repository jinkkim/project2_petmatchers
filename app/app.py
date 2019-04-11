#!/usr/bin/env python
import os
import pandas
import numpy
import sqlalchemy

from flask import Flask, jsonify


app = Flask(__name__)

#engine = create_engine("",
#    connect_args={'check_same_thread':False})
#
#Base = automap_base()
#Base.prepare(engine, reflect=True)
#
#session = Session(engine)

@app.route("/")
def home():
	return index.html




@app.route("/find")
def find():
	return find.html



@app.route("/information")
def info():
	return information.html


