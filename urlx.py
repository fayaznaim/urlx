#!/usr/bin/env python3

# TODO
# todo display the url if url and ip if ip typed - done
# todo see if I can differentiate between a domain name or a longer url.
# todo put the url data, the html in a variable to be able to re extract stuff.

from introscreen import *
from abuseipdb import *
from safewebnorton import *
from sucurinet import *
from talosintelligence import *
from threatminerorg import *
from urlvoid import *
from virustotalcom import *

new = 2  # open in a new tab, if possible


# introscreen()

urlx = input("  Enter a domain/url/ip address to get the analysis results:")
print("  You entered: ", urlx + "\n")

# The call of all the functions in
print("*****   RESULTS   *****")
abuseipdb(urlx)
safewebnorton(urlx)
sucurinet(urlx)
talosintelligence(urlx)
threatminerorg(urlx)
urlvoid(urlx)
virustotalcom(urlx)

print ("*****   End of output *****")
