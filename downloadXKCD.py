#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
"""
Webscraper that downloads xkcd comics
Checks if comic already downloaded so for increased efficiency on rerun.

Needs feature update where title text is in properties of downloaded image.

https://automatetheboringstuff.com/chapter11/
"""
import time
import os
import requests
import bs4


start = time.time()


def getPrevLink(soup, url):
    prevLink = soup.select('a[rel="prev"]')[0]
    return 'https://xkcd.com' + prevLink.get('href')


url = 'https://xkcd.com'              # starting url
os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd

while not url.endswith('#'):
    # Download the page.
    print('Downloading page {}...'.format(url))
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        try:
            comicUrl = 'https:' + comicElem[0].get('src')
            # Download the image.
            print('Downloading image {}...'.format(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Check if comic previously downloaded.
            imageFile = open(os.path.join('xkcd',
                                          os.path.basename(comicUrl)), 'xb')
        except requests.exceptions.MissingSchema:
            # skip this comic
            url = getPrevLink(soup, url)
            continue
        except FileExistsError:
            print('--- Comic already downloaded.---')
            # skip this comic
            url = getPrevLink(soup, url)
            continue
        # TODO: Needs feature update where title text
        #       is in properties of downloaded image.

        # Save the image to ./xkcd.
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # Get the Prev button's url.
    url = getPrevLink(soup, url)

print('Done.')

timetotal = time.time() - start
if timetotal > 60:
    mins = timetotal//60
    sec = timetotal-min*60
    print(f"Runtime: {mins} minutes, {sec} seconds")
else:
    print(f"Runtime: {timetotal} seconds")
