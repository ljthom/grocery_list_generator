from sqlalchemy import text
from pantry import engine

def get_ingredients(ingredient):
    with engine.connect() as conn:
        result = conn.execute(text(f"select * from recipes where ingredients like '{ingredient}'"))
        print(result.keys())
        for item in result:
            print(item)
