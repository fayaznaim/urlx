#!/usr/bin/env python3
from urllib import request
import urllib
import re


def sucurinet(urlx):
    sucurineturl = ("https://sitecheck.sucuri.net/results/" + urlx + "/")
    print("SITECHECK.SUCURI.NET: " + sucurineturl)
    # fp = urllib.request.urlopen(sucurineturl)  # this is the connection to the page?
    # sucuribytes = fp.read()
    # mystr = sucuribytes.decode("utf8")
    # fp.close()
    # score = re.findall("Site issues detected", mystr)
    # print("Issues detected: ", score)

