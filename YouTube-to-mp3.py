#get Pytube from pip (Python package installer)
from pytube import YouTube
from sys import argv
import os

# get user input
link = input("Enter a YouTube link you would like to download. (Enter 'q' to quit)\n")

def download_audio():
    yt = YouTube(link)

    # output title and views of video
    title = yt.title
    print("Title: ", title)
    views = '{:,}'.format(yt.views)
    print("Views: ", views)

    # filename
    name_of_file = input('What would you like to name the file? (Do not include .mp4)\n')
    name_of_file_complete = name_of_file + '.mp4'

    # make sure filename is unused in folder
    path = "C:\\Users\\phamh\\Desktop\\" + name_of_file_complete

    if os.path.exists(path):
        name_of_file = name_of_file + "(1)"
        name_of_file_complete = name_of_file + '.mp4'
        print("\"" + path + "\"" + " already exists, adding to filename")

    print("new filename: " + name_of_file_complete)

    # find top audio file for download
    res = ''
    for stream in yt.streams.filter(adaptive=True, audio_codec = 'mp4a.40.2'):
        
        if stream.resolution != res:
            print(stream.resolution)
        res = stream.resolution
        stream.download('C:/Users/phamh/Desktop', filename=name_of_file_complete)
        print("audio downloaded")
        break

    # make sure audio file exist in folder
    def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)

    find(name_of_file_complete, 'C:/Users/phamh/Desktop')
    print("audio found in Desktop folder")

while link != 'q':
    download_audio()
    link = input("Enter a YouTube link you would like to download. (Enter 'q' to quit)\n")