"""Flask app for adopt app."""

from flask import Flask

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def show_pets():
    """Show all the pets."""

    pets = Pet.query.all()

    return render_template(
                            "pet-list.html",
                            pets = pets)

@app.get("/add")
def show_add_pet_form():
    """Show form to add new pet."""

    return render_template(
                            "add-pet.html"
    )