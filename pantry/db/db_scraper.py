import argparse
import lxml
import os
import re
import requests
import time
import threading
import urllib.parse
from recipe_scrapers import scrape_me
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", nargs='+', help="Enter any number of URLs", required=False)
parser.add_argument("-n", "--num", help="Number of results to return", required=False)
args = parser.parse_args()

db = {}
urls = []
if args.url:
    for each in args.url:
         urls.append(each)
else:
    urls = ["https://www.zenbelly.com/post-sitemap1.xml", "https://www.zenbelly.com/post-sitemap2.xml", 
        "https://www.zenbelly.com/post-sitemap3.xml", "https://www.bodybuilding.com/sitemap-bbcomrecipe.xml", 
        "https://www.myrecipes.com/sitemaps/recipe/1/sitemap.xml", "https://www.marthastewart.com/sitemaps/recipe/1/sitemap.xml", 
        "https://www.marthastewart.com/sitemaps/recipe/2/sitemap.xml", "https://www.eatingwell.com/sitemaps/recipe/1/sitemap.xml", 
        "https://www.southernliving.com/sitemap_1.xml", "https://www.budgetbytes.com/post-sitemap.xml", 
        "https://www.budgetbytes.com/post-sitemap2.xml", "https://fitmencook.com/recipes-sitemap.xml", 
        "https://fitmencook.com/recipes-sitemap2.xml"]
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
            if counter >= int(args.num):
                break
            scraper = scrape_me(tag.strip())
            print(f"{threading.get_ident()} is processing: {scraper.canonical_url()}", end='\r', flush=True)
            db.update({tag:[scraper.title(), scraper.ingredients(), scraper.image()]})
            counter += 1
        except AttributeError:
            print(AttributeError)
        except TypeError:
            failed.append(f'{scraper.canonical_url()}')

if __name__ == '__main__':
    print(args.num)
    start = time.time()
    threads = []
    for i in range(len(urls)):
        thread = threading.Thread(target=scrape, args=(urls,i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
#    print(db)
    for each in db:
        print()
        print(db[each])
    print("Total time: ", time.time() - start)
#    print(failed)
