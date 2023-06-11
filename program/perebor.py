import os.path

def perebor ():

    path = '/home/kalinx/Desktop/program/video/'
    num_files = len([f for f in os.listdir(path)
                    if os.path.isfile(os.path.join(path, f))])
    sum_video = (num_files)
    print (sum_video)

perebor ()