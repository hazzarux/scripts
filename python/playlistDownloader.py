from barcode import get

__author__ = 'yigit'

import json

__author__ = 'yigit'

import urllib.request

# headers used for spider
HEADERS = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}


def getVideos(playlistNumber):
    '''
    returns a dictionary containing all the videos in a playlist
    key: title
    value: href
    '''
    videos={}
    url = "https://gdata.youtube.com/feeds/api/playlists/{0}?v=2&alt=json".format(playlistNumber)
    req = urllib.request.urlopen(url)
    inp = req.read().decode("utf-8")
    #print(inp)
    req.close()
    resp = json.loads(inp)
    returnedVideos = resp["feed"]["entry"]

    for video in returnedVideos:
        title = video["title"]["$t"]
        href = video["link"][0]["href"]
        videos[title]=href
    return videos


videos=getVideos("PLpuEs89VV9uqv5WIZcNkrGQKtED_RQKOi")
print(videos)