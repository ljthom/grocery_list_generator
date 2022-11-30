
from flask import redirect, render_template, request, url_for
from pantry import app
from pantry.db_utils import sites


@app.route("/", methods=["GET", "POST"])
def index(error=None):
    recipe_sites = sites
    if request.method == "POST":
        print("getting recipe selections: ")
        print()
        return redirect(url_for('ingredient_form'))

    return render_template('index.html', recipe_sites=recipe_sites, error=error)