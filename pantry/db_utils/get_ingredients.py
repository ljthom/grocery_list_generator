from sqlalchemy import text
from pantry import engine

def get_ingredients(ingredients):
    recipes = []
    results = []
    with engine.connect() as conn:
        if type(ingredients) == str:
            recipes = conn.execute(text("select url,ingredients,image from recipes where ingredients like :i"), {"i": "%" + ingredients + "%"}).fetchall()
            for each in recipes:
                result = {"url": each[0], "ingredients": each[1], "image": each[2]}
                results.append(result)
            print(len(results))
            return results
        elif len(ingredients) == 2:
            for ingredient in ingredients:
                recipes.append(conn.execute(text("select url,ingredients,image from recipes where ingredients like :i"), {"i": "%" + ingredient + "%"}).fetchall())
            for each in list(set(recipes[0]).intersection(recipes[1])):
                result = {"url": each[0], "ingredients": each[1], "image": each[2]}
                results.append(result)
            print(len(results))
            if len(results) > 10:
                return results[:10]
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
            print(len(results))
            if len(results) > 10:
                return results[:10]
            return results
