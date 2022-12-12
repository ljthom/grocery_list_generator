import json

from pantry import app
from flask import redirect, render_template, request, url_for


@app.route("/recipe_selection", methods=["GET", "POST"])
def recipe_selection(recipes=None, error=None):
    recipes = json.dumps(request.args.get('recipes', None))
    print(type(recipes))
    print(recipes)
    return render_template('recipe_selection.html', recipes=recipes, error=error)
