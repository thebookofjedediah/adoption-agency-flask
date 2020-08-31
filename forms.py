from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL


species_types = [
    "Dog", "Cat", "Porcupine"
]


class AddPetForm(FlaskForm):
    """Form for adding pets."""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[ (spe, spe) for spe in species_types])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age")
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing pets."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Notes")
    available = BooleanField("Available?")