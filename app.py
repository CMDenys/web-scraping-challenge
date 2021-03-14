from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_phone

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection 
app.config["MONGO_URI]"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():
    mars_full_dict = mongo.db.collection.find_one()
    return render_template("index.html", mars_full_dict=mars_full_dict)



# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    
    #run scrape function
    mars_data = scrape_mars.scrape_info()
    
    #update the Mongo database
    mongo.db.collection.update({}, mars_data, upsert=True)

    #redirect back to homepage


