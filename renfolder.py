import os
path='/home/vboxuser/Desktop/new-folder/assesment'
original=input("Enter the name of folder")
folder_path=os.path.join(path,original)
new_name=input('Enter a new name of folder')
new_path=os.path.join(path,new_name)


def renamefolder(): 
    try:
        os.rename(folder_path,new_path)
        print("renamed sucess")

    
    except:
        print("Error")
    

