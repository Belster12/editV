from moviepy.editor import *
import os.path
from natsort import natsorted


def rename_files(path, new_name, extention):
    os.chdir(path)
    
    for (i, filename) in enumerate(natsorted(os.listdir(path))):
        os.rename(src=filename, dst='{}{}{}' .format(new_name,i,extention))
        
rename_files('C:/editV-main4/program/video/', 'video', '.mp4' )



videosize = input('Введите значение:')


path = 'C:/editV-main4/program/video/'
num_files = len([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
sum_video = num_files
print(sum_video)

t = 10
start_time = 2

title = ImageClip("C:/editV-main4/program/Photo1.jpg").set_start(0).set_duration(t, change_end=True).set_pos(("center", "center")).set_opacity(0.7)
title = title.fx(vfx.resize, float(videosize))

for i in range(sum_video):
    clip = VideoFileClip(f'C:/editV-main4/program/video/video{i}.mp4')
    final = CompositeVideoClip([clip, title.set_position("center")])
    final = final.subclip(0, 7)
    final.write_videofile(f"C:/editV-main4/program/done/test{i}.mp4")