"""Flask app for adopt app."""

from flask import Flask, render_template, request, flash, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

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


@app.route("/add", methods=["GET", "POST"])
def add_new_pet():
    """Add pet form; handle adding and display of form."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        img = form.img.data or None
        age = form.age.data
        notes = form.notes.data

        flash(f"Added {name} to pet list")

        new_pet = Pet(name=name,
                    species=species,
                    img=img,
                    age=age,
                    notes=notes)

        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    else:
        return render_template(
            "add-pet-form.html", form=form)