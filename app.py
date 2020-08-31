from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Track what is happening during dev
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "hihihi333"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

# HOME PAGE ROUTE W/LIST
@app.route('/')
def get_home():
    """Home page, shows all pets"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/<int:pet_id>')
def show_pet_details(pet_id):
    """show details about a single pet"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet-details.html', pet=pet)