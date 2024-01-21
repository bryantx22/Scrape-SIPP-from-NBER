"""
Goal: Scrape .dct files from NBER's website

Author: Bryant Xia

Packages: requests, bs4, os
Last-updated: 07/30/2023
"""

import os
import requests
from bs4 import BeautifulSoup

url_dict = {
    "84": ("https://data.nber.org/sipp/1984/sip84w", "https://data.nber.org/sipp/1984/sip84rt"),
    "85": ("https://data.nber.org/sipp/1985/sip85w", "https://data.nber.org/sipp/1985/sip85rt"),
    "86": ("https://data.nber.org/sipp/1986/sip86w", "https://data.nber.org/sipp/1986/sip86rt"),
    "87": ("https://data.nber.org/sipp/1987/sip87w", "https://data.nber.org/sipp/1987/sip87rt"),
    "88": ("https://data.nber.org/sipp/1988/sip88w", "https://data.nber.org/sipp/1988/sip88rt"),
    "89": ("https://data.nber.org/sipp/1989/sip89w", "https://data.nber.org/sipp/1989/sip89rt"),
    "90": ("https://data.nber.org/sipp/1990/sip90w", "https://data.nber.org/sipp/1990/sip90t"),
    "91": ("https://data.nber.org/sipp/1991/sip91w", "https://data.nber.org/sipp/1991/sip91t"),
    "92": ("https://data.nber.org/sipp/1992/sip92w", "https://data.nber.org/sipp/1992/sip92t"),
    "93": ("https://data.nber.org/sipp/1993/sip93w", "https://data.nber.org/sipp/1993/sip93t"),
    "96": ("https://data.nber.org/sipp/1996/sip96l", "https://data.nber.org/sipp/1996/sip96t"), #1x issue
    "01": ("https://data.nber.org/sipp/2001/sip01w", "https://data.nber.org/sipp/2001/sip01t"),
    "04": ("https://data.nber.org/sipp/2004/sippl04puw", "https://data.nber.org/sipp/2004/sippp04putm"),
    "08": ("https://data.nber.org/sipp/2008/sippl08puw", "https://data.nber.org/sipp/2008/sippp08putm"),
}

type_dict = {
    "84": ("w", "rt"),
    "85": ("w", "rt"),
    "86": ("w", "rt"),
    "87": ("w", "rt"),
    "88": ("w", "rt"),
    "89": ("w", "rt"),
    "90": ("w", "tm"),
    "91": ("w", "tm"),
    "92": ("w", "tm"),
    "93": ("w", "tm"),
    "96": ("w", "tm"), #1x issue; NOTE that there is a TM in 1996 with 1x, which my code did not deal with; I downloaded this manually, but you can just add an if statement in the 'extract_helper' function
    "01": ("w", "tm"),
    "04": ("w", "tm"),
    "08": ("w", "tm"),
}

def scrape_and_save(url, dest):
    """
    url: string of the url intending to vist
    dest: file path for the .dct file. Should end in .txt. The function will change the extension to .dct.
    """

    r = requests.get(url)

    soup = BeautifulSoup(r.content, "html5lib")
    main_text = soup.find(
        "body"
    ).text  # the dictionary is contained exclusively within <body> </body>

    f = open(dest, "w+")
    f.write(main_text)
    f.close()

    pre, _ = os.path.splitext(dest)
    os.rename(dest, pre + ".dct")  # rename to dct files for Stata

def extract_helper(url1, url2, format1, format2, year):

    '''
    url1, format1: both strings, indicating the url of core panels and the short hand "w" for core panels
    url2, format2: both strings, indicating the url of topical modules and the short hand for topical modules (changes over time)
    '''

    dest_base = "CHANGE THIS TO WHERE YOU WANT TO STORE THE DCTs" 

    # Main loop for fetching .dct files
    for url, format in [(url1, format1), (url2, format2)]:
        for num in range(1, 17):
            '''
            Note that there are at most 16 waves or topical modules for any panels.
            I loop up to 16 for every panel; if it does not exit, the else statement deals with it.
            This is just to avoid figuring out exactly how many waves and TMs are in each panel.
            '''
            url_access = url + str(num) + ".dct"
            validate_url = requests.get(url_access)

            if validate_url.status_code == 200:
                requests.get(url_access)  # first test if the url is valid
                dest = dest_base + year + format + str(num) + ".txt" # Windows did not like saving as dct
                scrape_and_save(url_access, dest)
            else:
                print("Failed to access", format, num)
                print("The URL in question does not exist")

# extraction loop
for year in url_dict:
    url1, url2 = url_dict[year]
    format1, format2 = type_dict[year]

    extract_helper(url1, url2, format1, format2, year)
