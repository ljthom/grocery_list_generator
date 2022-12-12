import json

from pantry import app
from flask import redirect, render_template, request, url_for


@app.route("/recipe_selection", methods=["GET", "POST"])
def recipe_selection(error=None, recipes=None):
    print(recipes)
    return render_template('recipe_selection.html', recipes=recipes, error=error)
