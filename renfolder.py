import os



def renamefolder(old_path,new_path): 
    try:
        os.rename(old_path,new_path)
        print("renamed sucess")

    
    except:
        print("Error")
    

