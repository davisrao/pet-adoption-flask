"""Forms for adopt app."""

class AddSnackForm(FlaskForm):
    """Form for adding a pet."""

    name = StringField("Pet name")
    species = StringField("Species")
    img = StringField("Photo URL")
    age = StringField("Age")
    notes = StringField("Notes")