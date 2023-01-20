from dotenv import load_dotenv
load_dotenv()
from pytube import YouTube
import datetime
import os

file_path = os.getenv('FILE_PATH') #replace file path with your own

def download(link):
    youtubeVideo = YouTube(link)
    youtubeLength = str(datetime.timedelta(seconds=youtubeVideo.length)) #convert seconds to hours/minutes/seconds
    
    print('-' * 50)
    print('VIDEO INFORMATION:')
    print('Author: {}'.format(youtubeVideo.author))
    print('Title: {}'.format(youtubeVideo.title))  
    print('Length: {}'.format(youtubeLength))   
    print('Views: {}'.format(youtubeVideo.views))   
    print('-' * 50)
    
    to_download = input('Continue downloading this video? \n(y/n) ').casefold()
    
    if to_download == 'y':
        try:
            print('Downloading...........')
            youtubeVideo.streams.get_highest_resolution().download(file_path)
            print('Download completed!')
        except Exception as err:
            print(err)
            print('Error downloading video.')
    else:
        print('Exiting application.')
    
link = input('Youtube link: ')
download(link)
