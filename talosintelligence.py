#!/usr/bin/env python3
import webbrowser

def talosintelligence(urlx):
    talosurl = ("https://talosintelligence.com/reputation_center/lookup?search=" + urlx)
    print("TALOSINTELLIGENCE.COM: " + talosurl)
    #webbrowser.open(talosurl)