'''
Created on Apr 19, 2018

@author: dario
'''

# Project: multithreaded xkcd downloader

# multidownloadXkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading

# Step 1: Modify the Program to Use a Function
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd


def downloadXkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download page
        print("Downloading page http://xkcd.com/{}...".format(urlNumber))
        res = requests.get("http://xkcd.com/{}".format(urlNumber))
        res.raise_for_status()
        
        soup = bs4.BeautifulSoup(res.text)
        
        # Find the URL of the comic image.
        comicElem = soup.select("#comic img")
        if comicElem == []:
            print("Could not find comic image.")
        else:
            comicUrl = comicElem[0].get("src")
            # Download image.
            print("Downloading image {}...".format(comicUrl))
            # must add http: -> differ from book
            res = requests.get("http:" + comicUrl)
            res.raise_for_status()
            
            # Save image to ./xkcd.
            imageFile = open(
                os.path.join("xkcd", os.path.basename(comicUrl)), "wb")
            
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            
            imageFile.close()


# Step 2: Create and Start Threads
downloadThreads = []  # a list of all the Thread objects
for i in range(0, 1400, 100):  # loop 14 times, creates 14 threads
    downloadThread = threading.Thread(target=downloadXkcd, args=(i, i + 99))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Step 3: Wait for All Threads to End
for downloadThread in downloadThreads:
    downloadThread.join()

print("Done")

