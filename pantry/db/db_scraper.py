import argparse
import os
import re
import sqlite3
import time
import threading
import requests
import lxml
from recipe_scrapers import scrape_me
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Path to database file", required=False)
parser.add_argument("-n", "--num", help="Number of results to return", required=False)
parser.add_argument("-u", "--url", nargs='+', help="Enter any number of URLs", required=False)
args = parser.parse_args()

def scrape(urls, index):
    print()
    print(f"Processing {len(urls[index])} URLs from {urls[index]}")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    xml = requests.get(urls[index], timeout=5).text
    if "Forbidden" in xml:
        xml = requests.get(urls[index], headers=headers, timeout=5).text
    pages = BeautifulSoup(xml, 'lxml').find_all("loc")
#    pages = re.findall(r"(https?://\S+</loc>)", xml, re.MULTILINE)
    counter = 0
    for each in pages:
        tag = re.sub('<[^<]+?>', '', str(each))
        try:
            scraper = scrape_me(tag.strip())
            if scraper.ingredients():
                if args.num:
                    if counter >= int(args.num):
                        break
#            elif counter >= 2:
#                break
                print(f"{threading.get_ident()} is processing: {tag}", end='\r', flush=True)
                db.update({tag:[scraper.title(), scraper.canonical_url(), scraper.ingredients(), scraper.image()]})
                counter += 1
        except AttributeError:
            failed.append(tag)
        except TypeError:
            failed.append(tag)
        else:
            failed.append(tag)
            continue

if __name__ == '__main__':
    start = time.time()
    db = {}
    urls = []
    if args.file:
        if os.path.exists(args.file):
            try:
                conn = sqlite3.connect(args.file)
                cursor = conn.cursor()
            except sqlite3.Error as error:
                print("Failed to insert data into table", error)
        else:
            print("Unable to locate DB")
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
    threads = []
    for i in range(len(urls)):
        thread = threading.Thread(target=scrape, args=(urls,i))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print()
    for each in db:
        title = db.get(each)[0]
        url = db.get(each)[1]
        ingredients = db.get(each)[2]
        image = db.get(each)[3]
        items = (title, url, image)
        cursor.execute("INSERT OR REPLACE INTO recipes (title, url, image) VALUES (?, ?, ?)", items)
        for ingredient in ingredients:
            cursor.execute("INSERT OR REPLACE INTO recipes (ingredients) VALUES (?)", (ingredient, ))
    print(f"Committing into {args.file}...")
    conn.commit()
    cursor.close()
    conn.close()
    print(f"Processed {len(db)} recipes ...")
    print(f"{len(failed)} recipes failed ...")
    print("Total time: ", time.time() - start)
    for each in failed:
        print(each)
