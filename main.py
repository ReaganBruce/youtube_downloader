from dotenv import load_dotenv
load_dotenv()
from pytube import YouTube
from tqdm import tqdm
import datetime
import os

file_path = os.getenv('FILE_PATH') #replace file path with your own
ls_dir = os.listdir(file_path) #list items in directory

def download(link):
    youtube_video = YouTube(link)
    youtube_length = str(datetime.timedelta(seconds=youtube_video.length)) #convert seconds to hours/minutes/seconds
    
    print('-' * 50)
    print('Video Information:'.upper())
    print('Author: {0}'.format(youtube_video.author))
    print('Title: {0}'.format(youtube_video.title))  
    print('Length: {0}'.format(youtube_length))   
    print('Views: {0}'.format(youtube_video.views))   
    print('-' * 50)
    
    if len(ls_dir) != 0:
        print('Current files in directory:'.upper())
        for index, ls in enumerate(ls_dir):
            print('{0}. {1}'.format(index + 1, ls)) #enumerate over items in current directory and prints result at index 1
    else:
        print('Nothing found in directory: {0}'.format(file_path).upper())
    
    to_download = input('\nContinue downloading this video? \n(y/n) ').casefold() #second input
    
    if to_download == 'y':
        try:
            for i in tqdm(range(100), desc="Download In Progress", ncols = 100): #CLI progress bar module
                youtube_video.streams.get_highest_resolution().download(file_path)
            print('\nDownload completed at file location: {0}'.format(file_path))
        except Exception as err:
            print(err)
            print('Error downloading video.')
    else:
        print('Exiting application.')
    
link = input('Youtube link: ')
download(link)