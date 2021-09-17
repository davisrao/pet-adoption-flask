from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, AnyOf, URL

"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet name",
                        validators=[InputRequired()])
    species = StringField("Species",
                        validators=[InputRequired(),AnyOf(['dog','cat','porcupine'])])
    img = StringField("Photo URL",
                        validators=[URL(message="Please provide a valid URL")])
    age = SelectField("Age",
                        choices=[('baby','Baby'),
                                ('young','Young'),
                                ('adult','Adult'),
                                ('senior','Senior')]
                    )
    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing a pet."""
    img = StringField("Photo URL",
                        validators=[URL(message="Please provide a valid URL")])
    notes = StringField("Notes")
    available = BooleanField("Available")