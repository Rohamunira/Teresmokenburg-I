import urllib.parse
import playwright
import playwright.sync_api
import sys
import os
import urllib
import pathlib
import argparse
import numpy
from icecream import ic
parser = argparse.ArgumentParser(description = "sample using")
parser.add_argument('--urls', type = str, help = "website urls")
parser.add_argument('--chromium', type = str, help = "custom chromium path")
parser.add_argument('--output', type = str, help = "path to output file")
parser.add_argument('--headless', type = str, help = "toggle headless mode")
args = parser.parse_args()
link = args.urls if args.urls else "https://zealdocs.org"
chromium_app = args.chromium if args.chromium else ""
output = args.output if args.output else "output.txt"
use_headless = True if args.headless == "True" else False
if not pathlib.Path(output).exists():
    pathlib.Path(output).parent.mkdir(parents = True, exist_ok = True)
open(output, "at")
with playwright.sync_api.sync_playwright() as playwrights:
    if chromium_app:
        browser = playwrights.chromium.launch(
            headless = use_headless,
            executable_path = chromium_app,
            timeout = 100000
        )
    else:
        browser = playwrights.chromium.launch(
            headless = use_headless
        )
    context = browser.new_context()
    page = browser.new_page()
    def run(link):
        print("now opening: " + link)
        page.goto(link, timeout = 100000)
        links = page.locator("a")
        try:
            if links:
                for n in numpy.arange(links.count()):
                    urls = links.nth(n).get_attribute("href")
                    urls_info = urllib.parse.urlparse(urls)
                    if urls_info.scheme and urls_info.netloc:
                        with open(output, "rt") as f:
                            stored_link: numpy.ndarray = numpy.array(f.read().splitlines())
                            basic_url = urls_info.scheme + "://" + urls_info.netloc
                        for n in stored_link():
                            print(basic_url)
                        if not numpy.isin(basic_url, stored_link): # basic_url not in stored_link
                            with open(output, "at") as f:
                                f.write(basic_url + "\n")
                            print("found link: " + basic_url)
                            run(urls)
        except: pass
        with open(output, "rt") as f:
            stored_link: numpy.ndarray = numpy.array(f.read().splitlines())
            urls_info = urllib.parse.urlparse(link)
            basic_url = urls_info.scheme + "://" + urls_info.netloc
            if len(stored_link) == 1:
                next_url = stored_link[numpy.where(stored_link == basic_url)[0]] # stored_link.index(basic_url)
            else:
                if numpy.where(stored_link == basic_url)[0] == len(stored_link): # stored_link.index(basic_url) == len(stored_link) - 2
                    next_url = stored_link[numpy.where(stored_link == basic_url)[0] - 50] # stored_link.index(basic_url) - 50
                else:
                    # print(stored_link[numpy.where(stored_link == basic_url)])
                    next_url = stored_link[numpy.where(stored_link == basic_url)[0] + 1] # stored_link.index(basic_url) + 1
            print(("no new link found, now trying: " + next_url)[0])
            run(next_url[0])
    run(link = link)
