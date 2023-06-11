import os

from natsort import natsorted

def rename_files(path, new_name, extention):
    os.chdir(path)
    
    for (i, filename) in enumerate(natsorted(os.listdir(path))):
        os.rename(src=filename, dst='{}{}{}' .format(new_name,i,extention))
        
rename_files ('/home/kalinx/Desktop/program/video/', 'video', '.mp4' )