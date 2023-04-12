import os

def delete(path):
    name=input("Enter name of file you want to delete")

    os.rmdir(os.path.join(path,name))
    print('ok')
