import renfolder
import list
import crt_file
import del_file
import del_folder
import crt_folder
import cp_folder
import move_file
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
        list.list_dir()

    elif x=="2":
        crt_file.create_file()

    elif x=='3':
        crt_folder.createfolder()

    elif x=='4':
        renfolder.renamefolder()

    elif x=='5':
        del_file.delete()

    elif x=="6":
        del_folder.delete()

    elif x=="7":
        cp_folder.copy_folder()

    elif x=="8":
        cp_file.copy_file()

    elif x=="9":
        move_file.move()

    elif x=="10":
        hide.hide_folder()

    else:
        print("Incorrect keyword")
        break
