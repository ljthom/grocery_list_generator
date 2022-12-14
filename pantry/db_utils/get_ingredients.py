from sqlalchemy import text
from pantry import engine

def get_ingredients(ingredients):
    recipes = []
    results = []
    with engine.connect() as conn:
        if len(ingredients) == 1:
            recipes = conn.execute(text("select url,ingredients,image from recipes where ingredients like :i"), {"i": "%" + ingredients[0] + "%"}).fetchall()
            for each in recipes:
                result = {"url": each[0], "ingredients": each[1], "image": each[2]}
                results.append(result)
            return results
        elif len(ingredients) == 2:
            for ingredient in ingredients:
                recipes.append(conn.execute(text("select url,ingredients,image from recipes where ingredients like :i"), {"i": "%" + ingredient + "%"}).fetchall())
            for each in list(set(recipes[0]).intersection(recipes[1])):
                result = {"url": each[0], "ingredients": each[1], "image": each[2]}
                results.append(result)
            return results
        else:
            for ingredient in ingredients:
                recipes.append(conn.execute(text("select url,ingredients,image from recipes where ingredients like :i"), {"i": "%" + ingredient + "%"}).fetchall())
            final_recipes = list(set(recipes[0]).intersection(recipes[1]))
            for index in range(2, len(recipes)):
                final_recipes = set(final_recipes).intersection(recipes[index])
            for each in list(final_recipes):
                result = {"url": each[0], "ingredients": each[1], "image": each[2]}
                results.append(result)
            return results
