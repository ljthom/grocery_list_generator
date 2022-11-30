import json

from pantry import app
from flask import redirect, render_template, request, url_for


@app.route("/recipe_selection", methods=["GET", "POST"])
def recipe_selection(error=None):
    ingredients = None
    if request.method == "POST":
        ingredients = request.form.get('ingredient_name')
    return render_template('recipe_selection.html', ingredients=ingredients, error=error)
