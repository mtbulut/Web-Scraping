from flask import Flask,redirect, render_template
import scrape_mars, pymongo   # Mongo will be used in python.

# getting Flask 

app = Flask(__name__)

CONN = "mongodb://localhost:27017"