"""scrape 
This script is meant to help user grab rss link from html source of ytchannel.
This file contains these functions:
*getrss - returns the desired RSS 

Usage:
    Name = getrss(https://youtube.com/@ExampleChannel)
    print(name)
"""

import math
import urllib.request

import bs4 as bs


def getrss(channelName: str):
    """Function that gets rss from youtube channel source

    Args:
        channelName (str): Name of channel from which you want to extract rss

    Returns:
        fulllink(str): Rss from channel
    """
    try:
        with urllib.request.urlopen(channelName) as response:
            source = response.read()
            soup = bs.BeautifulSoup(source, "lxml")
            for script in soup.find_all("link", rel="alternate", title="RSS"):
                rssFound = script
            rssFound = str(rssFound)
            rssFound = rssFound.split()
            rssFound[1] = rssFound[1].split("=")
            fullLink = rssFound[1][1] + "=" + rssFound[1][2]
            return fullLink
    except urllib.error.URLError as e:
        print("There was problem with opening this url")
    except urllib.error.HTTPError as e:
        print("There was problem with opening this http")