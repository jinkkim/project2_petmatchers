#!/usr/bin/env python
import os
import pandas
import numpy
import sqlalchemy

from flask import Flask, render_template, jsonify


app = Flask(__name__)

#engine = create_engine("",
#    connect_args={'check_same_thread':False})
#
#Base = automap_base()
#Base.prepare(engine, reflect=True)
#
#session = Session(engine)

@app.route("/")
def index():
	return render_template("index.html")




@app.route("/find")
def find():
	return render_template("find.html")



@app.route("/information")
def info():
	return render_template("information.html")



if __name__ == "__main__":
    app.run(debug=True)
