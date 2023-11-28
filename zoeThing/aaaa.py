import tkinter 
import csv

root = tkinter.Tk()
root.geometry("400x600")

login_mainFrame = tkinter.Frame(root, bg="#565656")
mainframe = tkinter.Frame(login_mainFrame, bg="#606060")


def quiz():
    mainframe = tkinter.Frame(login_mainFrame, bg="#606060")
    mainframe.pack(fill=tkinter.BOTH, expand=True)

    back_button = tkinter.Button(mainframe, text="Back", font=("", 15), command=lambda: mainframe.pack_forget())
    back_button.place(x=10,y=10)
     
def login():
    username = username_entry.get()
    password = password_entry.get()
    with open('zoeThing/db.csv', mode='r') as f: # instead of zoeThing/db.csv , enter the folder the csv file and the python file are in follwed by the name of the csv file 
            myReader = csv.reader(f, delimiter=',')
            for row in myReader:
                if row[:2] == [username, password]:
                    print("Logged in successfully")
                    quiz()
                    return   
            return print("Try again")

def register():
    username = username_entry.get()
    password = password_entry.get()
    print(username + " " + password)
    with open('zoeThing/db.csv', mode='a') as f:
        myWriter = csv.writer(f, delimiter=',', lineterminator="\n")
        myWriter.writerow([username, password])  

login_mainFrame = tkinter.Frame(root, bg="#565656")
login_mainFrame.pack(fill=tkinter.BOTH, expand=True)

welcome_label = tkinter.Label(login_mainFrame, text="haii", font=("", 20), bg="#565656")
welcome_label.place(width=40, x=180,y=40)

username_label = tkinter.Label(login_mainFrame, text="Username", font=("", 15), bg="#565656")
username_entry = tkinter.Entry(login_mainFrame)
username_label.place(width=140, x=130,y=100)
username_entry.place(width=140, x=130,y=130)

password_label = tkinter.Label(login_mainFrame, text="Password", font=("", 15), bg="#565656")
password_entry = tkinter.Entry(login_mainFrame)
password_label.place(width=140, x=130,y=170)
password_entry.place(width=140, x=130,y=200)

login_button = tkinter.Button(login_mainFrame, text="Login", font=("",15), command=login)
register_button = tkinter.Button(login_mainFrame, text="Register", font=("",15), command=register)
login_button.place(width=60, height=30, x=130,y=300)
register_button.place(width=60, height=30, x=210, y=300)

root.mainloop()