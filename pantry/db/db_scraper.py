from recipe_scrapers import scrape_me
import urllib.parse
import threading
import requests
import re
import os
import time

item = {}
db = {}
#urls = ["https://fitmencook.com/recipes-sitemap2.xml"]
urls = ["https://www.budgetbytes.com/post-sitemap.xml", "https://www.budgetbytes.com/post-sitemap2.xml", "https://fitmencook.com/recipes-sitemap.xml", "https://fitmencook.com/recipes-sitemap2.xml"]
failed = []

def scrape(urls):
    print()
    print(f"Processing {len(urls)} URLs from {urls}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    xml = requests.get(urls).text
    if "Forbidden" in xml:
        xml = requests.get(urls, headers=headers).text
    pages = re.findall(r"(https?://\S+</loc>)", xml, re.MULTILINE)
    counter = 0
    for each in pages:
        tag = each.strip("</loc>")
        try:
            if counter > 10:
                break
            scraper = scrape_me(tag.strip())
            print(f"{os.getpid()} is processing: {scraper.canonical_url()}", end='\r', flush=True)
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
            failed.append(f'{scraper.canonical_url()}')

if __name__ == '__main__':
    start = time.time()
    for i in range(len(urls)):
        threading.Thread(target=scrape(urls[i])).start()
    print(db)
    print("Total time: ", time.time() - start)
    print(failed)
