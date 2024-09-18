from pytubefix import YouTube 

# link of the video to be downloaded 
links = []

with open('links.txt', 'r') as file:
    # Leggi tutte le righe e rimuovi eventuali spazi bianchi (come \n)
    links = [line.strip() for line in file]

for link in links:
    try: 
        # object creation using YouTube 
        yt = YouTube(link) 
    except: 
        #to handle exception 
        print("Connection Error") 

    # Get all streams and filter for mp4 files
    d_video = yt.streams.filter(file_extension='mp4').get_highest_resolution()

    try: 
        # downloading the video 
        d_video.download()
        print('Video downloaded successfully!\n')
    except: 
        print("Some Error!\n")

# Cancella il contenuto del file una volta finito
with open('links.txt', 'w') as file:
    # Scrivi una stringa vuota per cancellare il contenuto del file
    file.write("")