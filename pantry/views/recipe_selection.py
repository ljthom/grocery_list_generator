import json

from pantry import app
from flask import redirect, render_template, request, url_for
from pantry.db_utils.get_ingredients import get_ingredients


@app.route("/recipe_selection", methods=["GET", "POST"])
def recipe_selection(ingredients=None, error=None):
    ingredients = request.args.get('ingredients', None)
    query = get_ingredients(ingredients.split(','))
    for recipe in query:
        recipe_ingredients = eval(recipe.get('ingredients'))
        recipe['ingredients'] = recipe_ingredients
    if request.method == 'POST':
        print(request.form.getlist('recipe_return'))
    return render_template('recipe_selection.html', recipes=query, ingredients=ingredients, error=error)
