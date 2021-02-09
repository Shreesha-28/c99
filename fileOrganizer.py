import os
import shutil
#write the name of the directory that needs to be sorted
path=input("enter the name of the directory that needs to be sorted: ")

#create a properly organized list with all the files that are in the director
list_of_files=os.listdir(path)

#go through each and every file
for file in list_of_files:
    name,ext=os.path.splitext(file)

    #storing the extention
    ext=ext[1:]

    #forces the next loop if it is a directory
    if ext=='':
        continue
    
    #move the file to the directory if the name ext already
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)

    #create a new folder if the directroy doesnt exist
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
