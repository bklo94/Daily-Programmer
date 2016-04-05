from tkinter import *
import tkinter.messagebox

def openGrades():
    f= open("eemb179.txt")
    aboutStud.delete(1.0,END)

    studGradeString = ""

    for i in f:
        studGradeString += i

    aboutStud.insert(END, studGradeString)
    f.close()
    return

def openRank():
    f= open("eemb17.txt")
    aboutStud.delete(1.0,END)

    studGradeString = ""

    for i in f:
        studGradeString += i

    aboutStud.insert(END, studGradeString)
    f.close()
    return

def openFiles(selection):
    if selection == "Student Grades":
        openGrades()
    else:
        openRank()
    return

def saveGrades():
    gradeUpdate = aboutStud.get(1.0,END)
    outToFile = open('eemb179.txt','w')
    outToFile.write(gradeUpdate)
    outToFile.close()
    return

def aboutMe():
    tkinter.messagebox.showinfo("Hello")
    return

app = Tk()
app.title("Gui Example")
app.geometry("560x460+200+200")

menubar = Menu(app)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Open Grades",command=openGrades)
filemenu.add_command(label="Open Rank", command=openRank)

filemenu.add_separator()

filemenu.add_command(label="Quit", command=app.quit)
menubar.add_cascade(label="File",menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_cascade(label="About Me", command=aboutMe)
menubar.add_cascade(label="Help",menu=helpmenu)

app.config(menu=menubar)

aboutStud = Text(app)
aboutStud.insert(END, "Select student information above")
aboutStud.pack()

studFiles = StringVar()
studFiles.set(None)
files = ['Student Grades', "Student Rank"]
studDropDown = OptionMenu(app, studFiles, *files, command=openFiles).pack()

button1 = Button(app, text="Save Grades", width = 20, command=saveGrades)
button1.pack(side='bottom',padx=15,pady=15)

app.mainloop()
