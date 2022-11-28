import argparse
import json
import os
import re
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to database file", required=False)
args = parser.parse_args()

def connect():
    if args.file:
        if os.path.exists(args.file):
            try:
                global conn
                conn = sqlite3.connect(args.file)
                print(f"Connected to {args.file}")
            except sqlite3.Error as error:
                print("Failed to insert data into table", error)
        else:
            print("Unable to locate DB")

def query():
    global cursor
    global ingredients
    global results
    global titles
    global urls
    global meta
    cursor = conn.cursor()
#    results = cursor.execute("SELECT ingredients FROM recipes")
    ingredients = cursor.execute("SELECT ingredients from recipes").fetchall()
    results = cursor.execute("SELECT title, ingredients from recipes").fetchall()
    titles = cursor.execute("SELECT title from recipes").fetchall()
    urls = cursor.execute("SELECT url from recipes").fetchall()
#    meta = cursor.execute("SELECT ingredients, length(ingredients) from recipes ORDER BY length(ingredients) DESC").fetchall()
#    results = cursor.execute("SELECT * from recipes WHERE recipes.ingredients like ?", (ingredients,))

connect()
query()
recipes = []
final = []
for each in results:
    final.append(list(filter(lambda item: item is not None, each)))

#for each in final:
#    print(each)
#    while each not in titles:
#        print(' '.join(each))

for each in final:
    if each in titles[1]:   # NEED TO EXPAND THE TUPLES FROM TITLES TO CHECK
        print(each)

#print(recipes)
'''
for each in titles:
    if None not in each:
        print(each)
'''
#res = list(filter([i for i in results if i is not None]))
#res = list(filter(lambda item: item is not None, results))
#recipes = ' '.join(filter(lambda item: item is not None, res))
#print(recipes)

#recipe = []
#for each in res:
    #print(each[2])
#    recipes.append(each[2])
#recipe = [x for x in recipes if x is not None]
# THIS WORKS recipe = ' '.join(filter(lambda item: item is not None, recipes))

# Query database using SELECT * FROM recipes WHERE INGREDIENTS=

# Use regex to filter further

# print results (for now)
