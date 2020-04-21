#!/usr/bin/env python3

# TODO
# todo display the url if url and ip if ip typed - done
# todo see if I can differentiate between a domain name or a longer url.
# todo the talos link is not working. Now it is opening not sure what was wrong with it.
# todo put the url data, the html in a variable to be able to re extract stuff.

from introscreen import *
from urlvoid import *
from safewebnorton import *
from threatminerorg import *
from talosintelligence import *
from abuseipdb import *
new = 2  # open in a new tab, if possible


introscreen()

urlx = input("  Enter a domain/url/ip address to get the analysis results:")
print("  You entered: ", urlx + "\n")

# The call of all the functions in
print("         ****   RESULTS   ****")
urlvoid(urlx)
safewebnorton(urlx)
talosintelligence(urlx)
threatminerorg(urlx)
abuseipdb(urlx)

print ("\n\n*****   End of output *****")
