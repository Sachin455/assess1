import os
import shutil

def copy_folder():
    path='/home/vboxuser/Desktop/new-folder/assesment'
    name=input("Enter folder you want to copy")
    src_path=os.path.join(path,name)
    name2=input("Enter you destination")
    dst=os.path.join(path,name2,name)

    shutil.copytree(src_path,dst)
