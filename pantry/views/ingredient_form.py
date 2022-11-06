import json

from pantry import app
from flask import redirect, render_template, request, url_for


@app.route("/ingredient_form", methods=["GET", "POST"])
def ingredient_form(grocery_list=None, error=None):
    if grocery_list:
        data = json.loads(grocery_list)

    if request.method == "POST":
        if request.form.get('site_select_redirect'):
            return redirect(url_for('index'))
        if request.form.get('recipe_site'):
            selected_sites = request.form.getlist('recipe_site')
            print(selected_sites)
            # scrape_sites(selected_sites)
        if request.form.get('add_ingredient_entry'):
            print("Adding another Entry")

    return render_template('ingredient_form.html', error=error)
