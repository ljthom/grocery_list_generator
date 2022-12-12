import json

from pantry import app
from flask import redirect, render_template, request, url_for
from pantry.db_utils.get_ingredients import get_ingredients


@app.route("/grocery_list", methods=["GET", "POST"])
def grocery_list(ingredients=None, error=None):
    if request.method == 'POST':
        ingredients = []
        ingredients_selections = request.form.getlist('recipe_return')
        for ingredient_selection in ingredients_selections:
            ingredients += eval(ingredient_selection)

    return render_template('grocery_list.html', ingredients=ingredients, error=error)

