#!/usr/bin/env python3
import webbrowser
from urllib import request
import urllib
import re

def talosintelligence(urlx):
    talosurl = ("https://talosintelligence.com/reputation_center/lookup?search=" + urlx)
    print("TALOSINTELLIGENCE.COM: " + talosurl)
    # webbrowser.open(talosurl)