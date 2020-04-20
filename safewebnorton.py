#!/usr/bin/env python3
import webbrowser

def safewebnorton(urlx):
    safewebnortonurl = ("https://safeweb.norton.com/report/show?url=" + urlx)
    print("++++++++++++++++++++++++++++++++++++++++++++")
    print("SAFEWEB.NORTON.COM: " + safewebnortonurl)
    webbrowser.open(safewebnortonurl)