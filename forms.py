from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
"""Forms for adopt app."""

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet name")
    species = StringField("Species")
    img = StringField("Photo URL")
    age = SelectField("Age",
                        choices=[('baby','Baby'),
                                ('young','Young'),
                                ('adult','Adult'),
                                ('senior','Senior')]
                    )
    notes = StringField("Notes")