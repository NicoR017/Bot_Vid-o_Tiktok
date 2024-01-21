from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from historique import*
from modifVideo import*

def telecharger_et_superposer():
    video1_url = url_video1_entry.get()
    video2_url = url_video2_entry.get()
    nomVideo = nom_video_entry.get()

    if recherche_video("list.txt",video1_url)==True:
        # Téléchargement de la vidéo suppérieur
        yt = YouTube(video1_url)
        stream = yt.streams.first()
        stream.download(output_path=f'Video/{nomVideo}', filename=f'{nomVideo}.mp4')
        print("La vidéo principal est téléchargé")
        
        # Téléchargement de la vidéo inférieur
        yt = YouTube(video2_url)
        stream = yt.streams.first()
        stream.download(output_path=f'Video/{nomVideo}', filename=f'VideoInf.mp4')
        print("La vidéo inférieur est téléchargé")
        
    else:
        print("La vidéo a déja été téléchargé")

    chemin =f'Video/{nomVideo}'
    video1 = f'{chemin}/{nomVideo}.mp4'  
    video2 = f'{chemin}/VideoInf.mp4'

    superposer(video1,video2,chemin)

    video = f'{chemin}/video_superposee_avec_audio.mp4'

    couper_video(video,chemin)
    messagebox.showinfo("Notification", "La vidéo est prete")
    

# Création de l'interface utilisateur
root = Tk()

Label(root, text="URL Video Supérieur", font=("Helvetica", 14), bg="light grey").pack(pady=10)
url_video1_entry = Entry(root, font=("Helvetica", 12))
url_video1_entry.pack(pady=5)

Label(root, text="URL Video inférieur", font=("Helvetica", 14), bg="light grey").pack(pady=10)
url_video2_entry = Entry(root, font=("Helvetica", 12))
url_video2_entry.pack(pady=5)

Label(root, text="URL Nom Video", font=("Helvetica", 14), bg="light grey").pack(pady=10)
nom_video_entry = Entry(root, font=("Helvetica", 12))
nom_video_entry.pack(pady=5)

# Création du bouton pour lancer le téléchargement et la superposition des vidéosdownload_button = Button(root, text="Télécharger et superposer", command=telecharger_et_superposer, font=("Helvetica", 14), bg="blue", fg="white")
download_button = Button(root, text="Télécharger et superposer", command=telecharger_et_superposer, font=("Helvetica", 14), bg="black", fg="white")
download_button.pack(pady=20)

# Lancement de l'interface utilisateur
root.mainloop()
