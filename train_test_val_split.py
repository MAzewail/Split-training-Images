import os
import shutil
import numpy as np

path = '.\\test\\On\\'
#os.mkdir(path)
src = './training/On/'
for i in np.random.randint(0,len(os.listdir(src)),400):
    ext = str(i) + '.JPG'
    dst = os.path.join(path, ext)
    try:
        print('Moving' + ext)
        shutil.move((src + ext), dst)
    except:
        print('not found')