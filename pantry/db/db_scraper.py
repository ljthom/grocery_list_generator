from recipe_scrapers import scrape_me
from bs4 import BeautifulSoup
import lxml
import urllib.parse
import threading
import requests
import re
import os
import time

db = {}
#urls = ["https://www.marthastewart.com/sitemaps/recipe/1/sitemap.xml"]
urls = ["https://www.marthastewart.com/sitemaps/recipe/1/sitemap.xml", "https://www.marthastewart.com/sitemaps/recipe/2/sitemap.xml", "https://www.eatingwell.com/sitemaps/recipe/1/sitemap.xml", "https://www.southernliving.com/sitemap_1.xml", "https://www.budgetbytes.com/post-sitemap.xml", "https://www.budgetbytes.com/post-sitemap2.xml", "https://fitmencook.com/recipes-sitemap.xml", "https://fitmencook.com/recipes-sitemap2.xml"]
failed = []

def scrape(urls, index):
    print()
    print(f"Processing {len(urls[index])} URLs from {urls[index]}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    xml = requests.get(urls[index]).text
    if "Forbidden" in xml:
        xml = requests.get(urls[index], headers=headers).text
    pages = BeautifulSoup(xml, 'lxml').find_all("loc")
    #pages = re.findall(r"(https?://\S+</loc>)", xml, re.MULTILINE)
    counter = 0
    for each in pages:
        tag = re.sub('<[^<]+?>', '', str(each))
        try:
            if counter > 2:
                break
            scraper = scrape_me(tag.strip())
            if tag in db:
                continue
            print(f"{os.getpid()} is processing: {scraper.canonical_url()}", end='\r', flush=True)
            db.update({tag:[scraper.title(), scraper.ingredients()]})
            counter += 1
        except AttributeError:
            print(AttributeError)
        except TypeError:
            failed.append(f'{scraper.canonical_url()}')

if __name__ == '__main__':
    start = time.time()
    threads = []
    for i in range(len(urls)):
        thread = threading.Thread(target=scrape, args=(urls,i))
        threads.append(thread)
        thread.start()
#        threading.Thread(target=scrape(urls[i])).start()
    for thread in threads:
        thread.join()
    print(db)
    print("Total time: ", time.time() - start)
#    print(failed)
