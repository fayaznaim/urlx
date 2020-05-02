#!/usr/bin/env python3
from urllib import request
import urllib
import re


def urlvoid(urlx):
    urlvoidurl = ("https://urlvoid.com/scan/" + urlx + "/")
    #webbrowser.open(urlvoidurl)  # this works but only if the scan for a certain website has been done before.
    print("URLVOID.COM: " + urlvoidurl)
    fp = urllib.request.urlopen(urlvoidurl)  # this is the connection to the page?
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    score = re.findall("[0-9]{1,2}/[0-9]{2}", mystr)
    print("Score: ", score)

    # soup = BeautifulSoup(mystr, 'html.parser')
    # # print(soup.prettify()) # this will get everything.
    # # blacklist = soup.select("tr>td>span") # this works cant seem to get the exact text out of it.
    # blacklistline = soup.findAll("span", {"class": "label label-success"})
    # print(blacklistline)

