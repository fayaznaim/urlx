#!/usr/bin/env python3

# The following are the todo for this program and the overall purpose of it.
# todo display the url if url and ip if ip typed
# todo see if I can differntiate between a domain name or a longer url.
# todo see if any modifications need to done to the pasted url. - mostly done  - eachurl is different.
# todo the talos link is not working. Keeps opening in edge. force all to open in chrome I guess

#import webbrowser
from urllib import request
import urllib
from bs4 import BeautifulSoup
import re
from introscreen import *
from safewebnorton import *
new = 2  # open in a new tab, if possible


introscreen()


urlx = input("Enter a domain or an IP address to get the analysis URLS:")
print()
print("You entered: ", urlx)

def site_urlvoid():
    urlvoidurl = ("https://urlvoid.com/scan/" + urlx + "/")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("URLVOID.COM: " + urlvoidurl)
    webbrowser.open(urlvoidurl)  # this works but only if the scan for a certain website has been done before.
    # fp = urllib.request.urlopen(urlvoidurl)
    # mybytes = fp.read()
    # mystr = mybytes.decode("utf8")
    # fp.close()
    # #print(mystr)
    # soup = BeautifulSoup(mystr, 'html.parser')
    # # print(soup.prettify()) # this will get everything.
    # # blacklist = soup.select("tr>td>span") # this works cant seem to get the exact text out of it.
    # blacklistline = soup.findAll("span", {"class": "label label-success"})
    # print(blacklistline)


def site_talos():
    talosurl = ("https://talosintelligence.com/reputation_center/lookup?search=" + urlx)
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("TALOSINTELLIGENCE.COM: " + talosurl)
    webbrowser.open(talosurl)  # this works but only if the scan for a certain website has been done before.


def site_threatminerorg():
    threatminerurl = ("https://www.threatminer.org/domain.php?q=" + urlx)
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("THREATMINER.ORG: " + threatminerurl)
    webbrowser.open(threatminerurl)  # this works but only if the scan for a certain website has been done before.


# https://www.abuseipdb.com/check/ ip address.
def site_abuseipdb():
    abuseipdburl = ("https://www.abuseipdb.com/check/")


# The call of all the functions in

#site_urlvoid()
safewebnorton(urlx)
#site_talos()
#site_threatminerorg()
