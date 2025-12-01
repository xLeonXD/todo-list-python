import json
import os
file_name = "C:\\Users\\leon\\PyCharmMiscProject\\projects made by me\\back to python 2 week plan\\todolist.json"

def save_work(filename,x):
    if os.path.exists(filename):
        with open(filename,"r") as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    data = [data]  # convert single item into a list
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(x)
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
        print(f"{x} was added")

def check_work(filename):
    if os.path.exists(filename):
        with open(filename,"r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("error on check_work")
    else:
        data = []
    for i in data:
        print(i,end="\n")

def work_done(filename,x):
    if os.path.exists(filename):
        with open(filename,"r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("error on work_done")
    else:
        data = []
    work = 0
    num = 0
    for i in data:
        num += 1
        if x == i:
            z = f"{i} "+"- Done!"
            data.append(z)
            data.remove(i)
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
                print(f"{i} is now done!")
        elif x != i: # for stuff here you can just " if x in data "
            work += 1
    if work == num:
        print("work not found")

def remove_work(filename,x):
    if os.path.exists(filename):
        with open(filename,"r") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("error on remove_work")
    else:
        data = []
    if x in data:
        data.remove(x)
        with open(filename,"w") as file:
            json.dump(data,file,indent=4)
            print(f"{x} has been removed")
    else:
        print(f"{x} does not exist in list")

while True:
    print("What do you wanna do?")
    choice = input(f"check , add , done , remove ,  exit : ") # remove and done needs to be added
    if choice.lower() == "check":
        check_work(file_name)
    elif choice.lower() == "add":
        print("What do you want to add?")
        x = input()
        save_work(file_name,x)
    elif choice.lower() == "done":
        x = input("Which work is done?")
        work_done(file_name,x)
    elif choice.lower() == "remove":
        x = input("Which work do you wanna remove?")
        remove_work(file_name,x)
    elif choice.lower() == "exit":
        print("Exiting...")
        break

