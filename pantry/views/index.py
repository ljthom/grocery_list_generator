import json

from pantry import app, engine
from pantry.forms.ingredients_entry_form import IngredientEntryForm
from flask import redirect, render_template, request, url_for
from sqlalchemy import text

@app.route("/", methods=["GET", "POST"])
def ingredient_form(grocery_list=None, error=None):
    form = IngredientEntryForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print(form.ingredient.data)
            get_ingredients([form.ingredient.data])
    return render_template('ingredient_form.html', form=form, error=error)



def get_ingredients(ingredients):
    query = ["SELECT url FROM recipes WHERE ingredients like %"]
    for ingredient in ingredients:
        query.append(ingredient)
    print(query)
    ingredient = "%chicken"
    print(ingredient)
    with engine.connect() as conn:
        result = conn.execute(text("select url from recipes where ingredients like :i"), {"i": ingredient})
        for item in result:
            print(item)




        #result = conn.execute(recipes.query("SELECT * from recipes"))
        #result = conn.query(recipes).filter(Customers.name.like('sugar'))
        #results = conn.execute("recipes").filter("", "sugar")
        #query = conn.execute("SELECT url FROM recipes where ingredients like %s" % ingredients)
        #for each in query:
        #    print(each)

#def sort_results(data):
