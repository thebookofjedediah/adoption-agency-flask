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

# SHOW PET DETAILS
@app.route('/<int:pet_id>')
def show_pet_details(pet_id):
    """show details about a single pet"""
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet-details.html', pet=pet)

# CREATE NEW PET FORM
@app.route('/add')
def add_pet_form():
    """form to create a new pet"""
    return render_template('pet-form.html')

# CREATE THE NEW PET
@app.route('/add', methods=['POST'])
def create_new_pet():
    """Creating a new pet and go to home page"""
    name = request.form["name"]
    species = request.form["species"]
    photo_url = request.form["photo_url"]
    age = request.form["age"]
    notes = request.form["notes"]
    age = int(age) if age else None

    new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
    db.session.add(new_pet)
    db.session.commit()
    
    return redirect('/')