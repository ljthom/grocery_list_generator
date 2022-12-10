import json

from pantry import app, engine
from pantry.forms.ingredients_entry_form import IngredientEntryForm
from flask import redirect, render_template, request, url_for
from pantry.db_utils.get_ingredients import get_ingredients

@app.route("/", methods=["GET", "POST"])
def ingredient_form(grocery_list=None, error=None):
    form = IngredientEntryForm()
    if request.method == "POST":
        if form.validate_on_submit():
            get_ingredients(form.ingredient.data)
    return render_template('ingredient_form.html', form=form, error=error)

