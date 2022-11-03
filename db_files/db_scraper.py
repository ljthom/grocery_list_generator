from recipe_scrapers import scrape_me
import requests
import re

item = {}
db = {}

urls={1:"https://www.budgetbytes.com/post-sitemap.xml", 2:"https://www.budgetbytes.com/post-sitemap2.xml"}
for url in urls.values():
    xml = requests.get(url).text
    pages = re.findall("<loc>.*</loc>", xml)

    for each in pages:
        tag = each.strip("<loc>").strip("</loc>")
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
