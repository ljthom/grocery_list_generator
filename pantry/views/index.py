import json

from pantry import app, engine
from pantry.forms.ingredients_entry_form import IngredientEntryForm
from flask import redirect, render_template, request, url_for
#from pantry.views import recipe_selection
@app.route("/", methods=["GET", "POST"])
def ingredient_form(error=None):
    form = IngredientEntryForm()
    form.quantity.data = 1
    if request.method == "POST":
        if form.validate_on_submit():
            ingredients = form.ingredient.data
            return redirect(url_for('recipe_selection', ingredients=ingredients))

    return render_template('ingredient_form.html', form=form, error=error)

