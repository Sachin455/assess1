import os

def create_file():
    path='/home/vboxuser/Desktop/new-folder/assesment'
    name=input("Enter name of file")
    new_file=os.path.join(path,name)

    with open(new_file,'w') as file:
        file.write(" ok boys lets get going")

    with open(new_file,'r') as file:
        print(file.read())



