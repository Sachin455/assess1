import os

def create_file(path):
    name=input("Enter name of file")
    new_file=os.path.join(path,name)

    with open(new_file,'w') as file:
        file.write(" random text")

   # with open(new_file,'r') as file:
    #    print(file.read())



