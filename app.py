from pytube import YouTube

your_link = str(input("Enter Your YouTube Video Link: "))
YoutubeLink = YouTube(your_link)
config = YoutubeLink.streams.get_highest_resolution()

config.download()

print("Video Downloaded")