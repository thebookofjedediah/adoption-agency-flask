from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Track what is happening during dev
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "hihihi333"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

# HOME PAGE ROUTE
@app.route('/')
def get_home():
    return render_template('home.html')