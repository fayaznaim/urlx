#!/usr/bin/env python3

# The following are the todo for this program and the overall purpose of it.
#
# todo get url or domain from the user input. done.
# todo display the url - done.
# todo see if any modifications need to done to the pasted url. - mostly done  - eachurl is different.
# todo the talos link is not working. Keeps opening in edge. force all to open in chrome I guess

import webbrowser
from urllib import request
import urllib
from bs4 import BeautifulSoup
import re
new = 2 # open in a new tab, if possible


def introscreen():
    print("*** URL ANALYSIS SCRIPT FOR SCI CYBER ANALYSTS ***")
    print("\nThis program will open the desired url analysis sites with the user provided domain.\n"
          "Also displays the scraped text in the output below.\n\n"
          "[+] URLvoid, [+] Norton safeweb, [+] TALOS Intelligence,\n[+] ThreatMiner.org...more to be added\n")


def site_urlvoid():
    urlvoidurl = ("https://urlvoid.com/scan/" + urlx + "/")
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("opening: " + urlvoidurl)
    webbrowser.open(urlvoidurl) # this works but only if the scan for a certain website has been done before.
    fp = urllib.request.urlopen(urlvoidurl)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    #print(mystr)
    soup = BeautifulSoup(mystr, 'html.parser')
    #print(soup.prettify()) # this will get everything.
    print(soup.get_text()) # What I want is the report summary and text only.


def site_safewebnorton():
    nortonurl = ("https://safeweb.norton.com/report/show?url=" + urlx)
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("opening: " + nortonurl)
    webbrowser.open(nortonurl) # this works but only if the scan for a certain website has been done before.
    fp = urllib.request.urlopen(nortonurl)
    mbytes = fp.read()
    mystr = mbytes.decode("utf8")
    fp.close()
    soup = BeautifulSoup(mystr, 'html.parser')
    # print(soup.prettify())  # this will get everything.
    print(soup.get_text())


def site_talos():
    # https: // talosintelligence.com / reputation_center / lookup?search =
    talosurl = ("talosintelligence.com/reputation_center/lookup?search=" + urlx)
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("opening: " + talosurl)
    webbrowser.open(talosurl) # this works but only if the scan for a certain website has been done before.
    fp = urllib.request.urlopen(talosurl)
    mbytes = fp.read()
    mystr = mbytes.decode("utf8")
    fp.close()
    soup = BeautifulSoup(mystr, 'html.parser')
    # print(soup.prettify())  # this will get everything.
    print(soup.get_text())

def site_threatminerorg():
    # https: // www.threatminer.org / domain.php?q =
    threatminerurl = ("https://www.threatminer.org/domain.php?q=" + urlx)
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("opening: " + threatminerurl)
    webbrowser.open(threatminerurl) # this works but only if the scan for a certain website has been done before.
    fp = urllib.request.urlopen(threatminerurl)
    mbytes = fp.read()
    mystr = mbytes.decode("utf8")
    fp.close()
    soup = BeautifulSoup(mystr, 'html.parser')
    # print(soup.prettify())  # this will get everything.
    print(soup.get_text())


introscreen()
urlx = input("Enter a domain or a url for the analysis report:")
print()
print("You entered: ", urlx)  # urlx is a global variable


site_urlvoid()
site_safewebnorton()
# site_talos()
site_threatminerorg()


