import os
import shutil

def copy_file():
    path='/home/vboxuser/Desktop/new-folder/assesment'
    name=input("Enter file you want to copy")
    src_path=os.path.join(path,name)
    name2=input("Enter you destination")
    dst=os.path.join(path,name2,name)

    shutil.copy(src_path,dst)
    print('Check')

