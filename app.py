# use Flask to render a template, redirecting to another url, and creating a URL
# use Flask to render a template, redirecting to another url, and creating a URL
from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL
# The URI is saying that the app can reach Mongo through our localhost server, using port 27017, 
# using a database named "mars_app".
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Set Up App Routes
# uses PyMongo to find the "mars" collection in our database
# index.html is the default HTML file that we'll use to display the content we've scraped
# return an HTML template using an index.html file. 
# We'll create this file after we build the Flask routes
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# assign a new variable that points to our Mongo database
# referencing the scrape_all function in the scraping.py
# update the mongo db
# navigate our page back to / where we can see the updated content.
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

# The final bit of code we need for Flask is to tell it to run
if __name__ == "__main__":
   app.run()