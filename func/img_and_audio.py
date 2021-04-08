import os
from random import randrange

def img_selector():
    for root, dirs, files in os.walk('img\\memes', topdown=True):
        img_list = files
    return 'img\\memes\\' + img_list[randrange(len(img_list))]

def audio_selector():
    for root, dirs, files in os.walk('audio', topdown=True):
        audio_list = files
    return 'audio\\' + audio_list[randrange(len(audio_list))]

if __name__ == '__main__':
    print(audio_selector())