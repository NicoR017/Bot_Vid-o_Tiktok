from moviepy.editor import VideoFileClip
import cv2
import numpy as np

def couper_video(video_path, chemin):
    clip = VideoFileClip(video_path)
    duree_totale = clip.duration
    duree_coupe = 120  # Durée en secondes (2 minutes)

    time_points = list(range(0, int(duree_totale), duree_coupe))
    time_points.append(int(duree_totale))  # Ajouter la dernière durée

    for i in range(len(time_points) - 1):
        start_time = time_points[i]
        end_time = time_points[i + 1]
        subclip = clip.subclip(start_time, end_time)
        subclip.write_videofile(f"{chemin}/video_part_{i}.mp4")

    clip.close()

from moviepy.editor import VideoFileClip
import cv2

def superposer(videosup, videoinf, chemin):
    # Charger les vidéos
    video1 = cv2.VideoCapture(videosup)
    video2 = cv2.VideoCapture(videoinf)

    # Vérifier la validité des vidéos
    if not video1.isOpened() or not video2.isOpened():
        print("Erreur: Impossible d'ouvrir les vidéos.")
        return

    # Récupérer les propriétés des vidéos
    fps = video1.get(cv2.CAP_PROP_FPS)
    frame_width = int(video1.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video1.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Spécifier le codec pour l'écriture de la vidéo
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Créer un objet VideoWriter pour enregistrer la vidéo résultante
    out = cv2.VideoWriter(f'{chemin}/video_superposee.mp4', fourcc, fps, (frame_width, frame_height*2), isColor=True)

    # Superposer les images des deux vidéos
    while True:
        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()

        if not ret1 or not ret2:
            break

        # Redimensionner la frame2 pour qu'elle ait la même taille que la frame1
        frame2 = cv2.resize(frame2, (frame1.shape[1], frame1.shape[0]))

        # Superposer les images
        result = cv2.vconcat([frame1, frame2])

        # Enregistrer l'image superposée
        out.write(result)

    # Libérer les ressources
    video1.release()
    video2.release()
    out.release()
    cv2.destroyAllWindows()

    # Ajouter l'audio de la première vidéo à la vidéo superposée
    clip_video = VideoFileClip(f'{chemin}/video_superposee.mp4')
    clip_audio = VideoFileClip(videosup).audio
    final_clip = clip_video.set_audio(clip_audio)
    final_clip.write_videofile(f'{chemin}/video_superposee_avec_audio.mp4')

    print("La vidéo superposée avec l'audio de la première vidéo a été créée avec succès.")
