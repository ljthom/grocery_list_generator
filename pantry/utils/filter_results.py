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
            except sqlite3.Error as error:
                print("Failed to insert data into table", error)
        else:
            print("Unable to locate DB")

def query():
    global CURSOR
    global INGREDIENTS
    global TITLES
    global URLS
    CURSOR = conn.cursor()
    TITLES = CURSOR.execute("SELECT title from recipes").fetchall()
    INGREDIENTS = CURSOR.execute("SELECT title,ingredients from recipes").fetchall()
    URLS = CURSOR.execute("SELECT title,url from recipes").fetchall()
    IMAGES = CURSOR.execute("SELECT title,image from recipes").fetchall()

def stripall(data):
    global results
    results = []
    for each in data:
        results.append(list(filter(lambda item: item is not None, each)))
    return results

def build(ingredients, titles):
    a = stripall(ingredients)
    b = stripall(titles)
    c = {}
    counter = 0
    stored = ''
    for each in a:
        if each in b:
            stored = str(each)
            counter = 0
        elif counter > 0:
            c[stored].append(each)
        else:
            c.update({stored:[]})
            counter += 1
    return c

def printall(recipes):
    for key,value in recipes.items():
        temp = re.search(r'.*?\'(.*)\'.*', key)
        if temp is not None:
            print(f"Title:\t\t{temp.group(1)}")
            print(f"Ingredients:\t{value}")
            print(f"URL:\t\t{CURSOR.execute('SELECT url FROM recipes WHERE title like ?', [temp.group(1)]).fetchall()[0][0]}")
            print(f"Image:\t\t{CURSOR.execute('SELECT image FROM recipes WHERE title like ?', [temp.group(1)]).fetchall()[0][0]}")
        print()

if __name__ == '__main__':
    connect()
    query()
    recipes = build(INGREDIENTS, TITLES)
    printall(recipes)
