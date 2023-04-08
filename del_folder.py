import os

def delete():
    path='/home/vboxuser/Desktop/new-folder/assesment'
    name=input("Enter name of file you want to delete")
    path_loc=os.path.join(path,name)

    os.rmdir(path_loc)
    print('ok')

delete()