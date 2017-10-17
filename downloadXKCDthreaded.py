#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
"""
Webscraper that downloads xkcd comics
Checks if comic already downloaded so for increased efficiency on rerun.

Two run modess: Full and Quick
Full mode goes through every comic.
Quick mode quits when it reaches the first comic that is already downloaded.

Feature updates - multithreading, max 50 comics/thread.

Needs feature update where title text is in properties of downloaded image.

https://automatetheboringstuff.com/chapter11/
"""
import time
import os
import requests
import bs4
import threading

print('This script searches xkcd.com and downloads each comic.')

# User input for full run or until finding already downloaded comic.
print('There are two mode options:\n'
      '\nQuick mode: Or "refresh mode", checked until it finds '
      'a previously downloaded comic.\n'
      ' Full mode: Checks for every comic, downloads undownloaded comics.\n'
      )

while True:
    try:
        print('Please select mode:\n'
              'Enter 0 for Quick mode, or 1 for Full Mode')
        run_mode_selection = input('Mode: ')
        if int(run_mode_selection) == 0:
            run_mode = False  # Quick mode
            break
        if int(run_mode_selection) == 1:
            run_mode = True    # Full mode
            break
    except ValueError:
        continue

start = time.time()


os.makedirs('xkcd', exist_ok=True)   # store comics in ./xkcd


def download_xkcd(startComic, endComic):
    for urlNumber in range(startComic, endComic):
        # Download the page.
#        print(f'Downloading page http://xkcd.com/{urlNumber}...')
        try:
            res = requests.get(f'http://xkcd.com/{urlNumber}')
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, 'lxml')
        except requests.exceptions.HTTPError:
            continue
        # Find the URL of the comic image.
        comicElem = soup.select('#comic img')
        if comicElem == []:
            print(f'Could not find comic image {urlNumber}.')
        else:
            try:
                comicUrl = 'https:' + comicElem[0].get('src')
                # Download the image.
#                print(f'Downloading image {comicUrl}...')
                res = requests.get(comicUrl)
                res.raise_for_status()
                # Check if comic previously downloaded.
                imageFile = open(os.path.join(
                        'xkcd',
                        (f'{urlNumber} - {os.path.basename(comicUrl)}')), 'xb')

                # Save the image to ./xkcd
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

            # TODO: Needs feature update where title text
            #       is in properties of downloaded image.

            except requests.exceptions.MissingSchema:
                print(f'--- Missing comic {urlNumber}.---')
                continue  # skip this comic
            except FileExistsError:
                print(f'--- Comic {urlNumber} already downloaded.---')
                if run_mode:   # Full mode
                    continue  # skip this comic
                if not run_mode:
                    print(f'Finished updating archive, '
                          f'comics {startComic}-{endComic}.')
                    break


# Get latest comic number:
url = 'https://xkcd.com'
res = requests.get(url)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'lxml')
penultimateComic = soup.select('a[rel="prev"]')[0]
# penultimate Comic +1 for most recent comic
finalComicNum = int(penultimateComic.get('href')[1:-1]) + 1


# Create and start the Thread objects.
downloadThreads = []  # a list of all the Thread objects
for i in range(0, finalComicNum, 50):
    downloadThread = threading.Thread(target=download_xkcd, args=(i, i+49))
    downloadThreads.append(downloadThread)
    downloadThread.start()

# Wait for all threads to end.
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done.')

timetotal = time.time() - start
if timetotal > 60:
    mins = timetotal//60
    sec = timetotal-mins*60
    print(f"Runtime: {mins:.0f} minutes, {sec:.2f} seconds")
else:
    print(f"Runtime: {timetotal:.2f} seconds")

# if __name__ == "__main__":
    # execute only if run as a script
    # pass 0/1//True/False for run mode via main(mode)?
#    main(mode)
