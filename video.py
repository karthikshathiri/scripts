from pytube import YouTube
from pprint import pprint

print ('please enter the url : ')
url=input()
yt= YouTube(url)

print( '\n' + 'These are the videos available : ')
pprint(yt.get_videos())

print('\n'+yt.filename)
print('\n' + 'name the file name :')
name=input()

yt.set_filename(name)


print('\n'+'give codec :')
codec=input()

print('give resolution :')
res=input()

video = yt.get(codec,res)

print('\n'+'Downloading ....')
video.download('~/Music')

print('done')
