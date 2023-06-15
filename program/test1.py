import shutil
from moviepy.editor import *
import os.path
from natsort import natsorted
from pathlib import Path
import os

try:
    shutil.rmtree('/home/kalinx/Desktop/editV-main/program/done') 
except:



    try:
        # Переименование файлов видео
        def rename_files(path, new_name, extension):
            os.chdir(path)

            for (i, filename) in enumerate(natsorted(os.listdir(path))):
                os.rename(src=filename, dst='{}{}{}'.format(new_name, i, extension))

        rename_files('/home/kalinx/Desktop/editV-main/program/video/', 'video', '.mp4')

        # Размер видео
        videosize = input('Введите значение:')

        # Пересчет видео
        path = '/home/kalinx/Desktop/editV-main/program/video/'
        num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
        sum_video = num_files
        print(sum_video)

        folder_video = (5 * sum_video) // 25

        # Указание размеров видео
        for d in range(sum_video):
            clip = VideoFileClip(f'/home/kalinx/Desktop/editV-main/program/video/video{d}.mp4')
            resized_clip = clip.resize((576, 1024))
            resized_clip.write_videofile(f"/home/kalinx/Desktop/editV-main/program/video/video{d}.mp4")

        # Время по умолчанию
        t = 10
        start_time = 2

        # Изменение длительности видео
        title = ImageClip("/home/kalinx/Desktop/editV-main/program/Photo1.jpg").set_start(0).set_duration(t, change_end=True).set_pos(
            ("center", "center")).set_opacity(0.7)

        # Изменение размера видео
        title = title.fx(vfx.resize, float(videosize))

        for p in range(folder_video):
            os.makedirs('/home/kalinx/Desktop/editV-main/program/done/Video{p}', exist_ok=True)

        # Редактирование видео
        for h in range(folder_video):
            for j in range(6):
                i = (j * folder_video + h) % sum_video
                clip = VideoFileClip(f'/home/kalinx/Desktop/editV-main/program/video/video{i}.mp4')
                final = CompositeVideoClip([clip, title.set_position("center")])
                final = final.subclip(0, 7)
                final.write_videofile(f"/home/kalinx/Desktop/editV-main/program/done/video{h}test{i}_{j}.mp4", fps=clip.fps)


    except BrokenPipeError as e:
        print("Произошла ошибка BrokenPipeError:", e)

    except IOError as e:
        print("Произошла ошибка IOError:", e)

    except Exception as e:
        print("Произошла неизвестная ошибка:", e)
