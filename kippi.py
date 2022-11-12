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
    print("FOR HELP WRITE : kippi.py -h")
    #print(args)
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
def help():
    print("-----------------KIPPI DICTUNAURY--------------")
    print("-r [number tool] : run")
    print("-h : help")
    print("-u [File directory] : upload file")
    print("-l : Load latest database")
def PrintOptions():
    counter = 1
    options = getDB().split(',')
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
        WriteDB(getDB() + "," + open(args[1]).read())
        updatedContent = base64.b64decode(getDB().encode('ASCII')).decode('ASCII')
        repo.update_file("Database.db","Updated with " + args[1],updatedContent,repo.get_contents("Database.db").sha,"main")
    else:
        print("only database File!")

def WriteDB(text):
    db = open("Database.db","a")
    db.write(text)
def getDB():
    db = open("Database.db","r")
    print(db.read())
    return db.read()
if __name__ == '__main__':
    if not os.path.exists("Database.db"):
        LoadDB()
    startup()
