from pathlib import Path


def readfileandfolder():
    path=Path("")
    items = list(path.rglob("*"))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():

    try:
        print("Your current folder structure looks like this :  ")
        readfileandfolder()
        name = input("Please tell your file name :- ")
        p=Path(name)

        if not p.exists():
            with open(p,"w") as fs:
                data=input("What you want to write :-")
                fs.write(data)
            print(f"File Created Successfully")
        else:
            print("File already exists")
    except Exception as err:
        print(f"Error: {err}")

def readfile():

    try:
        print("Your current folder structure looks like this :  ")
        readfileandfolder()
        name = input("Enter which file do you want to read :-")
        p=Path(name)

        if p.exists():
            with open(p,"r") as fs:
                data=fs.read()
                print(data)

                print("Readed Successfully")
        else:
            print("File does not exist")
    except Exception as err:
        print(f"Error: {err}")


def updatefile():
    try:
        print("Your current folder structure looks like this :")
        readfileandfolder()

        name = input("Enter which file do you want to update :- ")
        p = Path(name)

        if p.exists():

            print("Press 1 to update the name of your file")
            print("Press 2 to overwrite the data in your file")
            print("Press 3 to append the data in your file")

            check = int(input("Enter your choice : "))

            if check == 1:
                newname = input("Enter the new name of your file :- ")
                p.rename(newname)
                print("Updated Successfully")

            elif check == 2:
                with open(p, "w") as fs:
                    data = input("What you want to write (overwrite your data) :- ")
                    fs.write(data)
                print("Updated Successfully")

            elif check == 3:
                with open(p, "a") as fs:
                    data = input("What you want to write (append your data) :- ")
                    fs.write(data)
                print("Updated Successfully")

            else:
                print("Invalid choice")

        else:
            print("File does not exist")

    except Exception as err:
        print(f"Error: {err}")


def deletefile():
    try:
        print("Your current folder structure looks like this :  ")
        readfileandfolder()
        name = input("Enter which file do you want to delete:-")
        p = Path(name)

        if p.exists():
            p.unlink()
            print("Deleted Successfully")
        else:
            print("File does not exist")

    except Exception as err:
        print(f"Error: {err}")



print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Please tell what do you want to do :- "))

if check==1:
    createfile()
if check==2:
    readfile()
if check==3:
    updatefile()
if check==4:
    deletefile()
