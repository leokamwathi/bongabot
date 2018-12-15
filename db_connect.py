'''
http://blog.y3xz.com/blog/2012/08/16/flask-and-postgresql-on-heroku


##
So now we need to add support for PostgreSQL. We’ll do that by using Flask-SQLAlchemy which will give us everything we need to connect to the Postgres DB as well as an easy to use ORM. So first we need to install the dependency and add it to our requirements.txt:
##

$ pip install flask-sqlalchemy psycopg2
# don't forget to update requirements.txt
$ pip freeze > requirements.txt

##
Before we continue we’ll have to create the Postgres DB and we’ll start off with the free dev plan which allows for up to 10K rows and 20 simultaneous connections:
##
$ heroku addons:add heroku-postgresql:dev
-----> Adding heroku-postgresql:dev to some-app-name... done, v196 (free)
Attached as HEROKU_POSTGRESQL_COLOR
Database has been created and is available

##
Once the database is setup we should promote it such that the DATABASE_URL environment variable will be set:
##
$ heroku pg:promote HEROKU_POSTGRESQL_COLOR
Promoting HEROKU_POSTGRESQL_COLOR_URL to DATABASE_URL... done

'''
###
#Now we can go ahead and import the library and add the basic connection boilerplate:
###

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)

###
#The next step is to commit the boilerplate code and create the actual DB tables:
###

'''
$ git commit -a -m "added DB boilerplate"
$ git push heroku master
# ...
$ heroku run python
'''

###
#Once we have a connected Python terminal we can run:
###

'''
>>> from app import db
>>> db.create_all()
'''

#####
#And we’re set! From here we can start using SQLAlchemy’s code to define models and create, query and delete objects. Here are some examples. We can start off by creating a new User model:
####

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name %r>' % self.name

###
#We can create the object itself:
###

user = User('John Doe', 'john.doe@example.com')
db.session.add(user)
db.session.commit()

###
#We can query objects:
###

user = User('John Doe', 'john.doe@example.com')
db.session.add(user)
db.session.commit()

###
#We can query objects:
###

all_users = User.query.all()

###
#And we can delete objects:
###

user = User('John Doe', 'john.doe@example.com')
db.session.delete(user)
db.session.commit()

###
#And that’s all you need to know about setting up a Flask + Postgres app on Heroku.
###