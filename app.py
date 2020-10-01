import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'blog'
app.config["MONGO_URI"] = 'mongodb+srv://root:Diamond12@myfirstcluster.geudv.mongodb.net/blog?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html", blog=mongo.db.movies.find())

@app.route('/add_tv')
def add_tv():
    return render_template('tv.html', blog=mongo.db.tv_shows.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
