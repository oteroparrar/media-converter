import os
import shutil
import time
from moviepy.editor import *
from decouple import config

# Directorio de entrada y salida
input_folder = config("FROM")
output_folder = config("TO")

# Elimina los archivos existentes en la carpeta de salida (opcional)
shutil.rmtree(output_folder)
os.makedirs(output_folder)

while True:
    # Recorre todos los archivos en la carpeta de entrada
    for filename in os.listdir(input_folder):
    
        # Carga el archivo de video
        video = VideoFileClip(os.path.join(input_folder, filename))

            # Reduce la resolución del video
        video_resized = video.resize(height=config("HEIHT"))

            # Reduce la tasa de bits del video
        video_resized.write_videofile(os.path.join(output_folder, filename),
                                          codec='libx264',
                                          bitrate='800k',
                                          audio_codec='aac',
                                          remove_temp=True)

            # Elimina el archivo original
        os.remove(os.path.join(input_folder, filename))
    
    # Espera 5 minutos antes de buscar archivos nuevos
    time.sleep(60)
