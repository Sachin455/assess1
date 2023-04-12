import os


def hide_folder(path,foldername):
    """

    """
   
    folderpath=os.path.join(path,foldername)

    os.rename(folderpath,os.path.join(path,"."+foldername))




