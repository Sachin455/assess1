import renfolder
import list
import crt_file
import del_file
import del_folder
import crt_folder
import cp_folder
import move_folder
import cp_file
import hide

while True:
    print("Enter 1 to list directories")
    print("Enter 2 to create file")
    print("Enter 3 to create folder")
    print("Enter 4 to rename file/folder")
    print("Enter 5 to delete file")
    print("Enter 6 to delete folder")
    print("Enter 7 to copy folder")
    print("Enter 8 to copy file")
    print("Enter 9 to move file or folder")
    print("Enter 10 to hide files")
    print("Enter 11 to toggle hideen files")
    print("Enter esc to exit")

    x=input("Enter your operation")

    if x=='esc':
        break

    elif x=='1':
        path=input("Enter path")
        list.list_dir(path)

    elif x=="2":
        path=input("Enter path")
        crt_file.create_file(path)

    elif x=='3':
        path=input("Enter location")
        crt_folder.createfolder(path)

    elif x=='4':
        old=input("Enter location of folder")
        new=input("Enter")
        renfolder.renamefolder()

    elif x=='5':
        path=input("Enter path")
        del_file.delete(path)

    elif x=="6":
        path=input("Enter path")
        del_folder.delete(path)

    elif x=="7":
        src=input("Enter the source you want to copy")
        dst=input("Enter destination location")
        cp_folder.copy_folder(src,dst)

    elif x=="8":
        src=input("Enter the source you want to copy")
        dst=input("Enter destination location")
        cp_file.copy_file(src,dst)

    elif x=="9":
        old=input("Enter location of file")
        new=input("Ener location where u want to move")
        move_folder.move(old,new)

    elif x=="10":
        path=input("Enter path")
        name=input("enter name")
        hide.hide_folder()

    else:
        print("Incorrect keyword")
        break
