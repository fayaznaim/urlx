#!/usr/bin/env python3
from urllib import request
import urllib
import re


def safewebnorton(urlx):
    safewebnortonurl = ("https://safeweb.norton.com/report/show?url=" + urlx)
    print("SAFEWEB.NORTON.COM: " + safewebnortonurl)
    fp = urllib.request.urlopen(safewebnortonurl)  # this is the connection to the page?
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    verdict = re.findall("SAFE|CAUTION", mystr)
    print(verdict)
