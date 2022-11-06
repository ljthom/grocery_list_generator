from flask import redirect, render_template, request, url_for
from pantry import app
from pantry.db import sites


@app.route("/", methods=["GET", "POST"])
def index(error=None):
    recipe_sites = sites
    if request.method == "POST":
        if request.form.get('get_sites'):
            print("Scraping Sites")
        return redirect(url_for('ingredient_form'))

    return render_template('index.html', recipe_sites=recipe_sites, error=error)
