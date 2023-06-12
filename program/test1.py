from moviepy.editor import *
import os.path
from natsort import natsorted

# Переименование файлов видео
def rename_files(path, new_name, extension):
    os.chdir(path)

    for (i, filename) in enumerate(natsorted(os.listdir(path))):
        os.rename(src=filename, dst='{}{}{}'.format(new_name, i, extension))

rename_files('C:/editV-main4/program/video/', 'video', '.mp4')

# Размер видео
videosize = input('Введите значение:')

# Пересчет видео
path = 'C:/editV-main4/program/video/'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
sum_video = num_files
print(sum_video)

folder_video = (5 * sum_video) // 25

# Указание размеров видео
for d in range(sum_video):
    clip = VideoFileClip(f'C:/editV-main4/program/video/video{d}.mp4')
    resized_clip = clip.resize((576, 1024))
    resized_clip.write_videofile(f"C:/editV-main4/program/video/video{d}.mp4")

# Время по умолчанию
t = 10
start_time = 2

# Изменение длительности видео
title = ImageClip("C:/editV-main4/program/Photo1.jpg").set_start(0).set_duration(t, change_end=True).set_pos(
    ("center", "center")).set_opacity(0.7)

# Изменение размера видео
title = title.fx(vfx.resize, float(videosize))

for f in range(folder_video):
    os.mkdir(f"C:/editV-main4/program/done/Video{f}")

# Редактирование видео
for h in range(folder_video):
    for j in range(6):
        i = (j * folder_video + h) % sum_video
        clip = VideoFileClip(f'C:/editV-main4/program/video/video{i}.mp4')
        final = CompositeVideoClip([clip, title.set_position("center")])
        final = final.subclip(0, 7)
        final.write_videofile(f"C:/editV-main4/program/done/Video{h}/test{i}_{j}.mp4")
