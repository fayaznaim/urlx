#!/usr/bin/env python3
from urllib import request
import urllib
import re
import hashlib

# get the input from user.
# if there is no http:  then add it.
# if there is no / at the end of the domain name then add it.
# get the sha256 of that domain in format https://google.com
# look into if it is https://  S
# make the fill url for virustotal.com and then option to open it.
# format : https://www.virustotal.com/gui/url/{sha256}/detection


def virustotalcom(urlx):
    urlx = "http://" + urlx + "/"
    inputhash = (hashlib.sha256(urlx.encode()))
    inputhashfinal = (inputhash.hexdigest())
    # print(inputhash.hexdigest())
    virustotalurl = ("https://www.virustotal.com/gui/url/" + inputhashfinal + "/detection")
    print("VIRUSTOTAL.COM: " + virustotalurl)




