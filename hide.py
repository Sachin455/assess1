import os
loc=input("ENter location")
foldername=input("Enter name of folder")

def hide_folder(path,foldername):
    """

    """
    folderpath=os.path.join(path,foldername)

    os.rename(folderpath,os.path.join(path,"."+foldername))




