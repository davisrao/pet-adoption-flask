from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, BooleanField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, Optional, AnyOf, URL

"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet name",
                        validators=[InputRequired()])
    species = StringField("Species",
                        validators=[InputRequired(),AnyOf(['dog','cat','porcupine'])])
    img = StringField("Photo URL",
                        validators=[URL(message="Please provide a valid URL"),Optional()])
    age = SelectField("Age",
                        choices=[('baby','Baby'),
                                ('young','Young'),
                                ('adult','Adult'),
                                ('senior','Senior')]
                    )
    
    notes = TextAreaField("Notes")

class EditPetForm(FlaskForm):
    """Form for editing a pet."""
    img = StringField("Photo URL",
                        validators=[URL(message="Please provide a valid URL"),Optional()])
    notes = StringField("Notes")
    available = BooleanField("Available")