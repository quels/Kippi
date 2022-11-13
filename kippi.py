import json
import sys
import os
import inspect
import base64
from github import Github
class Tool:
    def __init__(self,title,func):
        self.title = title
        self.functionCode = func
# Global varibles
args = sys.argv
args.pop(0)
g = Github("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")
repo = g.get_repo("quels/Kippi")

def Logo():
    print(" __  __     __     ______   ______   __  ")
    print("/\\ \\/ /    /\\ \\   /\\  == \\ /\\  == \\ /\\ \\  ")
    print("\\ \\  _\"-.  \\ \\ \\  \\ \\  _-/ \\ \\  _-/ \\ \\ \\ ")
    print(" \\ \\_\\ \\_\\  \\ \\_\\  \\ \\_\\    \\ \\_\\    \\ \\_\\ ")
    print("  \\/_/\\/_/   \\/_/   \\/_/     \\/_/     \\/_/ ")

def startup():
    Logo()
    print()
    if len(args) < 1:
        print("FOR HELP WRITE : kippi.py -h")
        PrintOptions()
    TranslateArgs()

def TranslateArgs():
    if len(args) > 0:
        if args[0] == "-h":
            help()
        if args[0] == "-l":
            LoadDB()
        if args[0] == "-r":
            if(len(args)>1):
                RunFunction()
            else:
                print("-r [number tool] : run")
        if args[0] == "-u":
            if(len(args)>1):
                AddTool()
            else:
                print("-u [File directory] : upload file")

def RunFunction():
    eval(getDB().split('\n')[int(args[1]) - 1].split(':')[1])

def help():
    print("-----------------KIPPI DICTUNAURY--------------")
    print("-r [number tool] : run")
    print("-h : help")
    print("-u [File directory] : upload file")
    print("-l : Load latest database")

def PrintOptions():
    counter = 1
    options = getDB().split('\n')
    for option in options:
        print(f"[{counter}] {option.split(':')[0]}")
        counter+= 1

def LoadDB():
    try:
        os.remove("Database.db")
        content = repo.get_contents("Database.db")
        content = content.decoded_content.decode('utf-8')
        WriteDB(content)
    except:
        content = repo.get_contents("Database.db")
        content = content.decoded_content.decode('utf-8')
        WriteDB(content)
    
def AddTool():
    if args[1].split('.')[1] == "db":
        LoadDB()
        WriteDB("\n" + open(args[1],"r").read())
        updatedContent = base64.b64encode(getDB().encode('ASCII')).decode('ASCII')
        repo.update_file("Database.db","Updated with " + args[1],getDB(),repo.get_contents("Database.db").sha,"main")
    else:
        print("only database File!")

def WriteDB(text):
    db = open("Database.db","a")
    db.write(text)

def getDB():
    db = open("Database.db","r")
    return db.read()

if __name__ == '__main__':
    if not os.path.exists("Database.db"):
        LoadDB()
    startup()
