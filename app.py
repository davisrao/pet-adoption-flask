"""Flask app for adopt app."""
import os
from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

API_SECRET_KEY = os.environ['API_SECRET_KEY']
API_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJOR2RMMld6N2QzOGJ5WnhJbmhydDJock40WFdETmJHSnFPb1ZWeEpORHZ6c09tWjZhWiIsImp0aSI6IjI0YzVmYzU3MTI2NWFkY2JhNTA3NGM5NDVmNzk1ZjFkNzQ3YWFlMzg3NDRlNWRlOWZjODU0ZjQzYmJkZTU2Y2M0N2E1YWMwNzA2ODU5ODk4IiwiaWF0IjoxNjMxOTIyMDI2LCJuYmYiOjE2MzE5MjIwMjYsImV4cCI6MTYzMTkyNTYyNiwic3ViIjoiIiwic2NvcGVzIjpbXX0.SGgKLYc3UR3UQ4ATXCBRVjHtDqiGVgD5b8oAxCpUSbcujqGP5hs0HeaA2Onu2aSIR4x3JLqAyfaN4lWA0PdlxYfDY-sAPffQaWopP4SCg9HefaGr7EE9IuyEJBefmbCy6K_MTK6wDubsTO8E0JiuNBC5YRMZ6UIragGiYB71_EpWlpNz0Q2dYb2h0x1pPrhxqxSpQ3MTbzgUCPZR3UrEZYl9Mu2QOtyOFJBeFbfjCmZYT1SE7fjHGByrfmj9Zt6W3zRrdgKTokjFuq2ei-1VdNi3a-ZtG6dN2uL5bRQ-kuGwYmUa7OUdZvAyLiXFxMs4u2DoJ2zFAdV6SkBIFi_uuA'

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

    return render_template("pet-list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def show_and_handle_new_pet_form():
    """Add pet form; handle adding and display of form."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        img = form.img.data or None
        age = form.age.data
        notes = form.notes.data


        new_pet = Pet(name=name,
                    species=species,
                    img=img,
                    age=age,
                    notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} to pet list")

        return redirect("/")

    else:
        return render_template(
            "add-pet-form.html", form=form)

@app.route("/<int:pet_id>", methods=["GET","POST"])
def edit_pet_details(pet_id):
    """Edit pet details form; handle editing or displaying a form"""

    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.img = form.img.data or None
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()

        flash(f"Successfully edited the details for {pet.name}")

        return redirect(f"/{pet.id}")

    else:
        return render_template("pet-details.html", pet=pet, form=form)
