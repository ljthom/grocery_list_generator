from recipe_scrapers import scrape_me
import requests
import re

# give the url as a string, it can be url from any site listed below
#scraper = scrape_me('https://www.allrecipes.com/recipe/158968/spinach-and-feta-turkey-burgers/')
item = {}
db = {}
counter = 0

urls={1:"https://www.budgetbytes.com/post-sitemap.xml", 2:"https://www.budgetbytes.com/post-sitemap2.xml", 3:"https://fitmencook.com/recipes-sitemap.xml", 4:"https://fitmencook.com/recipes-sitemap2.xml"}
for url in urls.values():
    xml = requests.get(url).text
    pages = re.findall("<loc>.*</loc>", xml)

    for each in pages:
        tag = each.strip("<loc>").strip("</loc>")
        try:
            if counter > 10:
                break
            scraper = scrape_me(tag.strip())
            print(f"Processing: {scraper.canonical_url()}")
            item.update({"title":scraper.title()})
            item.update({"url":scraper.canonical_url()})
            item.update({"ingredients":scraper.ingredients()})
            item.update({"time":scraper.total_time()})
            item.update({"nutrients":scraper.nutrients()})
            db.update({tag:item})
            counter += 1
        except AttributeError:
            print(AttributeError)
        except TypeError:
            print(f"No Schema found for the url {scraper.canonical_url()}")

print(db)
