from pytube import YouTube, Playlist

def pVideo(tag):
   URL = input("Enter playlist URL: ")
   playlist_url = URL
   p = Playlist(playlist_url)
   for url in p.video_urls:
      try:
         yt = YouTube(url)
      except VideoUnavailable:
         try:
            print(f'Video "{yt.title}" is unavaialable, skipping.')
         except:
            print(f'Video "{URL}" is unavaialable, skipping.')
         
      else:
      
         v_streams = yt.streams.get_by_itag(tag)
         try:
            print(f'downloading: "{video.title}"')
         except:
            print(f'downloading: "{URL}"')
         v_streams.download()
         
   print("download completed.")
   pass

def pAudio():
   pVideo(251)
   pass
#
#
#
def sVideo(tag):
   URL = input("Enter video URL: ")
   video = YouTube(URL)
   
   #print(video.streams)
   #v_streams = video.streams.filter(progressive = False, file_extension = 'mp3').get_by_itag(22)
   
   v_streams = video.streams.get_by_itag(tag)
   try:
      print(f'downloading: "{video.title}"')
      print("filepath:",v_streams.download())
   except:
      print(f'downloading: "{URL}"')
   
   print("download completed.")
   
   pass
   
def sAudio():
   sVideo(251)
   pass



def downloaderThing(format, size):
   if format == "1" and size == "1":
      pAudio()
   elif format == "1" and size == "2":
      sAudio()
      
   elif format == "2" and size == "1":
      pVideo(251)
   elif format == "2" and size == "2":
      sVideo(22)
   pass

###################################################################
   
downloadFormat = input("Do you want to download: \n1. only AUDIO\n2. VIDEO & AUDIO\n____________________\n")
downloadSize = input("\n\nDo you want to download: \n1. PLAYLIST\n2. ONE file\n____________________\n")

#22 = mp4 + 720p
#251 = mp3 + 160 kbps

downloaderThing(downloadFormat, downloadSize)