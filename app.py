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
def get_blog():
    return render_template("tasks.html", tasks=mongo.db.blog.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
