from moviepy.editor import *
import os.path
import os
from natsort import natsorted

print ("Размер картинкии вводите в формате: 0.1/n или же  0.75")
sizee = input("Введите размер изображения:  ")

def rename_files(path, new_name, extention):
    os.chdir(path)
    
    for (i, filename) in enumerate(natsorted(os.listdir(path))):
        os.rename(src=filename, dst='{}{}{}' .format(new_name,i,extention))
        
rename_files ('/home/kalinx/Desktop/program/video/', 'video', '.mp4' )


path = '/home/kalinx/Desktop/program/video/'
num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])
sum_video = (num_files)
print (sum_video)



t = 10  # Продолжительность заголовка
start_time = 2  # Время начала заголовка




title = ImageClip("/home/kalinx/Desktop/program/Photo1.jpg").set_start(0).set_duration(t, change_end=True).set_pos(("center","center")).set_opacity(0.7)
title = title.fx(vfx.resize, sizee)  #Ресайз переписал в формате 0.0. Как по мне так удобнее




if sum_video == 1:
# 1. Импорт видео
    
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')

# 2. Склейка видео и фото(местоположении фотографии)
    
    final = CompositeVideoClip([clip, title.set_position("center")])

# 3. Обрезка клипа по 0.7 секунд
    
    final = final.subclip(0, 7)

# 4. Запись конечного файла
    
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")



elif sum_video == 2:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    
                                            
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")

elif sum_video == 3:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])    
    
    
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    
                                        
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")

elif sum_video == 4:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    clip3 = VideoFileClip('/home/kalinx/Desktop/program/video/video3.mp4')
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])
    final3 = CompositeVideoClip([clip3, title.set_position("center")])
    
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    final3 = final3.subclip(0, 7)
    
                                    
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")
    final3.write_videofile("/home/kalinx/Desktop/program/done/test3.mp4")
    
elif sum_video == 5:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    clip3 = VideoFileClip('/home/kalinx/Desktop/program/video/video3.mp4')
    clip4 = VideoFileClip('/home/kalinx/Desktop/program/video/video4.mp4')
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])
    final3 = CompositeVideoClip([clip3, title.set_position("center")])
    final4 = CompositeVideoClip([clip4, title.set_position("center")])
    
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    final3 = final3.subclip(0, 7)
    final4 = final4.subclip(0, 7)
                                
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")
    final3.write_videofile("/home/kalinx/Desktop/program/done/test3.mp4")
    final4.write_videofile("/home/kalinx/Desktop/program/done/test4.mp4")

elif sum_video == 6:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    clip3 = VideoFileClip('/home/kalinx/Desktop/program/video/video3.mp4')
    clip4 = VideoFileClip('/home/kalinx/Desktop/program/video/video4.mp4')
    clip5 = VideoFileClip('/home/kalinx/Desktop/program/video/video5.mp4')
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])
    final3 = CompositeVideoClip([clip3, title.set_position("center")])
    final4 = CompositeVideoClip([clip4, title.set_position("center")])
    final5 = CompositeVideoClip([clip5, title.set_position("center")])
    
        
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    final3 = final3.subclip(0, 7)
    final4 = final4.subclip(0, 7)
    final5 = final5.subclip(0, 7)
    
                            
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")
    final3.write_videofile("/home/kalinx/Desktop/program/done/test3.mp4")
    final4.write_videofile("/home/kalinx/Desktop/program/done/test4.mp4")
    final5.write_videofile("/home/kalinx/Desktop/program/done/test5.mp4")
    
elif sum_video == 7:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    clip3 = VideoFileClip('/home/kalinx/Desktop/program/video/video3.mp4')
    clip4 = VideoFileClip('/home/kalinx/Desktop/program/video/video4.mp4')
    clip5 = VideoFileClip('/home/kalinx/Desktop/program/video/video5.mp4')
    clip6 = VideoFileClip('/home/kalinx/Desktop/program/video/video6.mp4')
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])
    final3 = CompositeVideoClip([clip3, title.set_position("center")])
    final4 = CompositeVideoClip([clip4, title.set_position("center")])
    final5 = CompositeVideoClip([clip5, title.set_position("center")])
    final6 = CompositeVideoClip([clip6, title.set_position("center")])
    
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    final3 = final3.subclip(0, 7)
    final4 = final4.subclip(0, 7)
    final5 = final5.subclip(0, 7)
    final6 = final6.subclip(0, 7)
    
                        
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")
    final3.write_videofile("/home/kalinx/Desktop/program/done/test3.mp4")
    final4.write_videofile("/home/kalinx/Desktop/program/done/test4.mp4")
    final5.write_videofile("/home/kalinx/Desktop/program/done/test5.mp4")
    final6.write_videofile("/home/kalinx/Desktop/program/done/test6.mp4")
    
    
    
elif sum_video == 8:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    clip3 = VideoFileClip('/home/kalinx/Desktop/program/video/video3.mp4')
    clip4 = VideoFileClip('/home/kalinx/Desktop/program/video/video4.mp4')
    clip5 = VideoFileClip('/home/kalinx/Desktop/program/video/video5.mp4')
    clip6 = VideoFileClip('/home/kalinx/Desktop/program/video/video6.mp4')
    clip7 = VideoFileClip('/home/kalinx/Desktop/program/video/video7.mp4')
    
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])
    final3 = CompositeVideoClip([clip3, title.set_position("center")])
    final4 = CompositeVideoClip([clip4, title.set_position("center")])
    final5 = CompositeVideoClip([clip5, title.set_position("center")])
    final6 = CompositeVideoClip([clip6, title.set_position("center")])
    final7 = CompositeVideoClip([clip7, title.set_position("center")])
    
        
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    final3 = final3.subclip(0, 7)
    final4 = final4.subclip(0, 7)
    final5 = final5.subclip(0, 7)
    final6 = final6.subclip(0, 7)
    final7 = final7.subclip(0, 7)
    
                    
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")
    final3.write_videofile("/home/kalinx/Desktop/program/done/test3.mp4")
    final4.write_videofile("/home/kalinx/Desktop/program/done/test4.mp4")
    final5.write_videofile("/home/kalinx/Desktop/program/done/test5.mp4")
    final6.write_videofile("/home/kalinx/Desktop/program/done/test6.mp4")
    final7.write_videofile("/home/kalinx/Desktop/program/done/test7.mp4")

elif sum_video == 9:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    clip3 = VideoFileClip('/home/kalinx/Desktop/program/video/video3.mp4')
    clip4 = VideoFileClip('/home/kalinx/Desktop/program/video/video4.mp4')
    clip5 = VideoFileClip('/home/kalinx/Desktop/program/video/video5.mp4')
    clip6 = VideoFileClip('/home/kalinx/Desktop/program/video/video6.mp4')
    clip7 = VideoFileClip('/home/kalinx/Desktop/program/video/video7.mp4')
    clip8 = VideoFileClip('/home/kalinx/Desktop/program/video/video8.mp4')
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])
    final3 = CompositeVideoClip([clip3, title.set_position("center")])
    final4 = CompositeVideoClip([clip4, title.set_position("center")])
    final5 = CompositeVideoClip([clip5, title.set_position("center")])
    final6 = CompositeVideoClip([clip6, title.set_position("center")])
    final7 = CompositeVideoClip([clip7, title.set_position("center")])
    final8 = CompositeVideoClip([clip8, title.set_position("center")])    
    
    
    
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    final3 = final3.subclip(0, 7)
    final4 = final4.subclip(0, 7)
    final5 = final5.subclip(0, 7)
    final6 = final6.subclip(0, 7)
    final7 = final7.subclip(0, 7)
    final8 = final8.subclip(0, 7)
    
                
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")
    final3.write_videofile("/home/kalinx/Desktop/program/done/test3.mp4")
    final4.write_videofile("/home/kalinx/Desktop/program/done/test4.mp4")
    final5.write_videofile("/home/kalinx/Desktop/program/done/test5.mp4")
    final6.write_videofile("/home/kalinx/Desktop/program/done/test6.mp4")
    final7.write_videofile("/home/kalinx/Desktop/program/done/test7.mp4")
    final8.write_videofile("/home/kalinx/Desktop/program/done/test8.mp4")
    
elif sum_video == 10:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    clip3 = VideoFileClip('/home/kalinx/Desktop/program/video/video3.mp4')
    clip4 = VideoFileClip('/home/kalinx/Desktop/program/video/video4.mp4')
    clip5 = VideoFileClip('/home/kalinx/Desktop/program/video/video5.mp4')
    clip6 = VideoFileClip('/home/kalinx/Desktop/program/video/video6.mp4')
    clip7 = VideoFileClip('/home/kalinx/Desktop/program/video/video7.mp4')
    clip8 = VideoFileClip('/home/kalinx/Desktop/program/video/video8.mp4')
    clip9 = VideoFileClip('/home/kalinx/Desktop/program/video/video9.mp4')
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])
    final3 = CompositeVideoClip([clip3, title.set_position("center")])
    final4 = CompositeVideoClip([clip4, title.set_position("center")])
    final5 = CompositeVideoClip([clip5, title.set_position("center")])
    final6 = CompositeVideoClip([clip6, title.set_position("center")])
    final7 = CompositeVideoClip([clip7, title.set_position("center")])
    final8 = CompositeVideoClip([clip8, title.set_position("center")])
    final9 = CompositeVideoClip([clip9, title.set_position("center")])    
    
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    final3 = final3.subclip(0, 7)
    final4 = final4.subclip(0, 7)
    final5 = final5.subclip(0, 7)
    final6 = final6.subclip(0, 7)
    final7 = final7.subclip(0, 7)
    final8 = final8.subclip(0, 7)
    final9 = final9.subclip(0, 7)
    
            
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")
    final3.write_videofile("/home/kalinx/Desktop/program/done/test3.mp4")
    final4.write_videofile("/home/kalinx/Desktop/program/done/test4.mp4")
    final5.write_videofile("/home/kalinx/Desktop/program/done/test5.mp4")
    final6.write_videofile("/home/kalinx/Desktop/program/done/test6.mp4")
    final7.write_videofile("/home/kalinx/Desktop/program/done/test7.mp4")
    final8.write_videofile("/home/kalinx/Desktop/program/done/test8.mp4")
    final9.write_videofile("/home/kalinx/Desktop/program/done/test9.mp4")
    
elif sum_video == 11:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    clip3 = VideoFileClip('/home/kalinx/Desktop/program/video/video3.mp4')
    clip4 = VideoFileClip('/home/kalinx/Desktop/program/video/video4.mp4')
    clip5 = VideoFileClip('/home/kalinx/Desktop/program/video/video5.mp4')
    clip6 = VideoFileClip('/home/kalinx/Desktop/program/video/video6.mp4')
    clip7 = VideoFileClip('/home/kalinx/Desktop/program/video/video7.mp4')
    clip8 = VideoFileClip('/home/kalinx/Desktop/program/video/video8.mp4')
    clip9 = VideoFileClip('/home/kalinx/Desktop/program/video/video9.mp4')
    clip10 = VideoFileClip('/home/kalinx/Desktop/program/video/video10.mp4')
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])
    final3 = CompositeVideoClip([clip3, title.set_position("center")])
    final4 = CompositeVideoClip([clip4, title.set_position("center")])
    final5 = CompositeVideoClip([clip5, title.set_position("center")])
    final6 = CompositeVideoClip([clip6, title.set_position("center")])
    final7 = CompositeVideoClip([clip7, title.set_position("center")])
    final8 = CompositeVideoClip([clip8, title.set_position("center")])
    final9 = CompositeVideoClip([clip9, title.set_position("center")])
    final10 = CompositeVideoClip([clip10, title.set_position("center")])    
    
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    final3 = final3.subclip(0, 7)
    final4 = final4.subclip(0, 7)
    final5 = final5.subclip(0, 7)
    final6 = final6.subclip(0, 7)
    final7 = final7.subclip(0, 7)
    final8 = final8.subclip(0, 7)
    final9 = final9.subclip(0, 7)
    final10 = final10.subclip(0, 7)
    
        
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")
    final3.write_videofile("/home/kalinx/Desktop/program/done/test3.mp4")
    final4.write_videofile("/home/kalinx/Desktop/program/done/test4.mp4")
    final5.write_videofile("/home/kalinx/Desktop/program/done/test5.mp4")
    final6.write_videofile("/home/kalinx/Desktop/program/done/test6.mp4")
    final7.write_videofile("/home/kalinx/Desktop/program/done/test7.mp4")
    final8.write_videofile("/home/kalinx/Desktop/program/done/test8.mp4")
    final9.write_videofile("/home/kalinx/Desktop/program/done/test9.mp4")
    final10.write_videofile("/home/kalinx/Desktop/program/done/test10.mp4")
    
elif sum_video == 12:
    clip = VideoFileClip('/home/kalinx/Desktop/program/video/video0.mp4')
    clip1 = VideoFileClip('/home/kalinx/Desktop/program/video/video1.mp4')
    clip2 = VideoFileClip('/home/kalinx/Desktop/program/video/video2.mp4')
    clip3 = VideoFileClip('/home/kalinx/Desktop/program/video/video3.mp4')
    clip4 = VideoFileClip('/home/kalinx/Desktop/program/video/video4.mp4')
    clip5 = VideoFileClip('/home/kalinx/Desktop/program/video/video5.mp4')
    clip6 = VideoFileClip('/home/kalinx/Desktop/program/video/video6.mp4')
    clip7 = VideoFileClip('/home/kalinx/Desktop/program/video/video7.mp4')
    clip8 = VideoFileClip('/home/kalinx/Desktop/program/video/video8.mp4')
    clip9 = VideoFileClip('/home/kalinx/Desktop/program/video/video9.mp4')
    clip10 = VideoFileClip('/home/kalinx/Desktop/program/video/video10.mp4')
    clip11 = VideoFileClip('/home/kalinx/Desktop/program/video/video11.mp4')    
    
    final = CompositeVideoClip([clip, title.set_position("center")])
    final1 = CompositeVideoClip([clip1, title.set_position("center")])
    final2 = CompositeVideoClip([clip2, title.set_position("center")])
    final3 = CompositeVideoClip([clip3, title.set_position("center")])
    final4 = CompositeVideoClip([clip4, title.set_position("center")])
    final5 = CompositeVideoClip([clip5, title.set_position("center")])
    final6 = CompositeVideoClip([clip6, title.set_position("center")])
    final7 = CompositeVideoClip([clip7, title.set_position("center")])
    final8 = CompositeVideoClip([clip8, title.set_position("center")])
    final9 = CompositeVideoClip([clip9, title.set_position("center")])
    final10 = CompositeVideoClip([clip10, title.set_position("center")])
    final11 = CompositeVideoClip([clip11, title.set_position("center")])
    
    final = final.subclip(0, 7)
    final1 = final1.subclip(0, 7)
    final2 = final2.subclip(0, 7)
    final3 = final3.subclip(0, 7)
    final4 = final4.subclip(0, 7)
    final5 = final5.subclip(0, 7)
    final6 = final6.subclip(0, 7)
    final7 = final7.subclip(0, 7)
    final8 = final8.subclip(0, 7)
    final9 = final9.subclip(0, 7)
    final10 = final10.subclip(0, 7)
    final11 = final11.subclip(0, 7)
    
    final.write_videofile("/home/kalinx/Desktop/program/done/test.mp4")
    final1.write_videofile("/home/kalinx/Desktop/program/done/test1.mp4")
    final2.write_videofile("/home/kalinx/Desktop/program/done/test2.mp4")
    final3.write_videofile("/home/kalinx/Desktop/program/done/test3.mp4")
    final4.write_videofile("/home/kalinx/Desktop/program/done/test4.mp4")
    final5.write_videofile("/home/kalinx/Desktop/program/done/test5.mp4")
    final6.write_videofile("/home/kalinx/Desktop/program/done/test6.mp4")
    final7.write_videofile("/home/kalinx/Desktop/program/done/test7.mp4")
    final8.write_videofile("/home/kalinx/Desktop/program/done/test8.mp4")
    final9.write_videofile("/home/kalinx/Desktop/program/done/test9.mp4")
    final10.write_videofile("/home/kalinx/Desktop/program/done/test10.mp4")
    final11.write_videofile("/home/kalinx/Desktop/program/done/test11.mp4")





          

