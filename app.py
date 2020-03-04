from flask import Flask, redirect, render_template
import scrape_mars
import pymongo 

# getting Flask

app = Flask(__name__)

CONN = "mongodb://localhost:27017"
client = pymongo.MongoClient(CONN)
db = client.mars_db


@app.route("/")
def index():
    mars_data = db.marsdata.find_one()
    mars_data = scrape_mars.scrape()
    return render_template("index.html", mars=mars_data)


@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    print(mars_data)
    db.marsdata.drop()
    db.marsdata.insert_one(mars_data)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
