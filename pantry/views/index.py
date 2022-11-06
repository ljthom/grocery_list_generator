import os

from pantry import app
from flask import redirect, render_template, request, url_for


@app.route("/", methods=["GET", "POST"])
def index(error=None):
    print(os.getcwd())
    if request.method == "POST":
        if request.form.get('get_sites'):
            print("Scraping Sites")
        return redirect(url_for('ingredient_form'))

    return render_template('index.html', error=error)
