#!/usr/bin/env python3
from urllib import request
import urllib
import re

def threatminerorg(urlx):
    threatminerurl = ("https://www.threatminer.org/domain.php?q=" + urlx)
    print("THREATMINER.ORG: " + threatminerurl)
    #webbrowser.open(threatminerurl)