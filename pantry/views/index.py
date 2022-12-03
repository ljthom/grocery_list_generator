import json

from pantry import app
from pantry.forms.ingredients_entry_form import IngredientEntryForm
from flask import redirect, render_template, request, url_for


@app.route("/", methods=["GET", "POST"])
def index(grocery_list=None, error=None):
    form = IngredientEntryForm()
    if grocery_list:
        data = json.loads(grocery_list)

    if request.method == "POST":
        if request.form.get('site_select_redirect'):
            return redirect(url_for('index'))
        if request.form.get('recipe_site'):
            selected_sites = request.form.getlist('recipe_site')
        if request.form.get('find_recipe'):
            ingredients = request.form.get('ingredient_name')
            print(ingredients)

    return render_template('ingredient_form.html', form=form, error=error)
