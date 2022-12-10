import json

from pantry import app
from pantry.forms.ingredients_entry_form import IngredientEntryForm
from flask import redirect, render_template, request, url_for
import sqlalchemy


@app.route("/ingredient_form", methods=["GET", "POST"])
def ingredient_form(grocery_list=None, error=None):
    form = IngredientEntryForm()
    if grocery_list:
        data = json.loads(grocery_list)
        print(data)

    if request.method == "POST":
        if request.form.get('site_select_redirect'):
            return redirect(url_for('index'))
        if request.form.get('recipe_site'):
            selected_sites = request.form.getlist('recipe_site')
        if request.form.get('find_recipes'):
            ingredients = request.form.get('ingredient_name')
            ingredients = ["chicken", "lettuce"]
            get_ingredients(ingredients)
            print(ingredients)
    return render_template('ingredient_form.html', form=form, error=error)

def get_ingredients(ingredients):
    engine = sqlalchemy.create_engine("sqlite:///pantry/models/recipes.db")
    query = ["SELECT url FROM recipes WHERE ingredients like %"]
    for ingredient in ingredients:
        query.append(ingredient)
    print(query)
    ingredient = "%chicken"
    print(ingredient)
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text("select url from recipes where ingredients like :i"), {"i": ingredient})
        for item in result:
            print(item)




        #result = conn.execute(recipes.query("SELECT * from recipes"))
        #result = conn.query(recipes).filter(Customers.name.like('sugar'))
        #results = conn.execute("recipes").filter("", "sugar")
        #query = conn.execute("SELECT url FROM recipes where ingredients like %s" % ingredients)
        #for each in query:
        #    print(each)
'''
connection = engine.connect()
myvar = 'jsmith' # our intended usage
myvar = 'jsmith or 1=1' # this will return all users
myvar = 'jsmith; DROP TABLE users' # this drops (removes) the users table
query = "select username from users where username = %s" % myvar
result = connection.execute(query)
for row in result:
    print "username:", row['username']
'''

#def sort_results(data):
