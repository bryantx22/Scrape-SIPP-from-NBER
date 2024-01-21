"""
Goal: Scrape .dct files from NBER's website

Author: Bryant Xia

Overview: Currently automates getting all the .dct files from the 2008 panel (core + topical module)
Packages: requests, bs4, os
"""

import requests
import zipfile
import io
from bs4 import BeautifulSoup

all_raw = "CHANGE THIS TO WHERE YOU WANT TO STORE THE RAW FILES"

url_link = "https://www.nber.org/research/data/survey-income-and-program-participation-sipp"
result = requests.get(url_link).text
soup = BeautifulSoup(result, 'html.parser')

data = soup.find_all('a', href = True) # this is what gives the download links from examining the html
TOTAL = 114
count = 0

bad_links = [] # links somehow we cannot download using this method; may need to print by hand
panel_indicator = { "w" + str(x) for x in range(1, 17)}

for link in data:

    if link['href'].find(".zip") != -1:

        # this contains a link
        # not neceessarily core or tm
        # downloading all for the moment

        is_panel = False
        for ind in panel_indicator:
            if link['href'].find(ind) != -1:
                is_panel = True
                break

        if is_panel: 
            count += 1
            try:
                r = requests.get(link['href'])
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(all_raw)
            except Exception as e:
                print(link['href'], " failed to open. The error message is ", str(e))
                bad_links.append(link['href'])

            print("Finished ", count, " out of ", TOTAL)

print(bad_links)




