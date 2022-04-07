import os
from os import path,system
import keyboard
import logging
import sys

def lock(cd):
    cmd = 'attrib +h +s "'+cd+'"'
    system(cmd)
    return

def unlock(cd):
    cmd = 'attrib -h -s "'+cd+'"'
    system(cmd)
    return

def keysup():
    key = keyboard.read_key()
    return(key)

def cdhere():
    cd = path.abspath(path.split(__file__)[0])
    return(cd)

def cdhere2():
    if getattr(sys, 'frozen', False):
        cd = os.path.dirname(sys.executable)
        running_mode = 'Frozen/executable'
    else:
        try:
            app_full_path = os.path.realpath(__file__)
            cd = os.path.dirname(app_full_path)
            running_mode = "Non-interactive (e.g. 'python myapp.py')"
        except NameError:
            cd = os.getcwd()
            running_mode = 'Interactive'
    return(cd)

def spaces(nb):
    for i in range (0, nb):
        print()
    return

def clear():
    system("cls")
    return

def createfolder(cd):
    cmd = 'mkdir "'+cd+'"'
    system(cmd)
    return

def deletefolder(cd):
    cmd = 'rmdir "'+cd+'"'
    system(cmd)
    return

def createfile(message,cd):
    cmd = 'echo '+message+' > "'+cd+'"'
    system(cmd)
    return

def deletefile(cd):
    return

def ListFolder(cd,NameFile):
    List = os.listdir(cd)
    List2 = list()
    for Folder in List:
        if os.path.isdir(os.path.join(cd, Folder)):
            List3 = os.listdir(cd+"\\"+Folder)
            if NameFile in List3:
                List2.append(Folder)
                print("-",Folder)
    return(List2)

def ListFolder2(cd):
    List = os.listdir(cd)
    List2 = list()
    for Folder in List:
        if os.path.isdir(os.path.join(cd, Folder)):
            List2.append(Folder)
            #print(Folder)
    return(List2)

# def ListFolder(cd):
#     List = os.listdir(cd)
#     max = int(len(List))
#     i = 0
#     while max > i :
#         if os.path.isdir(os.path.join(cd, List[i])):
#             print(List[i])
#         i = i + 1
#     return

def FindFile(cd,NameFile):
    f = open(cd+"\\"+NameFile, "r")
    Pwd = f.read()
    f.close()
    return(Pwd)

def Off():
    keyboard.press_and_release('del')
    return

def OpenFolder(cd):
    os.startfile(os.path.realpath(cd))
    return
