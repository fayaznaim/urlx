#!/usr/bin/env python3
from urllib import request
import urllib
import re


def securitytrailscom(urlx):
    securitytrailscomurl = ("https://securitytrails.com/domain/" + urlx + "/dns")
    print("SECURITYTRAILS.COM : " + securitytrailscomurl)