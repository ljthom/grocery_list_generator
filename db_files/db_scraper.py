from recipe_scrapers import scrape_me
import requests
import re

# give the url as a string, it can be url from any site listed below
#scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
item = {}
db = {}
counter = 0

with open('/root/Desktop/sites.txt', 'r') as reader:
    lines = reader.readlines()
    for each in lines:
        try:
            scraper = scrape_me(each.strip())
            print(scraper.canonical_url())
            item.update({"title":scraper.title()})
            item.update({"url":scraper.canonical_url()})
            item.update({"ingredients":scraper.ingredients()})
            item.update({"time":scraper.total_time()})
            item.update({"nutrients":scraper.nutrients()})
            db.update({each:item})
        except AttributeError:
            print("Error")

print(f"Items = {item}")
print(f"db = {db}")
