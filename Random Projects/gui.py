from tkinter import *
import tkinter.messagebox

#creates a popup message box
def beenClicked():
    radioValue = relStatus.get()
    tkinter.messagebox.showinfo("You clicked", radioValue)
    return

#changes the label and inserts it 
def changeLabel():
    name ="Thanks for the click " + yourName.get()
    labelText.set(name)
    yourName.delete(0,END)
    yourName.insert(0,"My name is Brandon")
    return
    

app = Tk()
app.title("Learning Python GUI")
app.geometry('450x300+200+200')


#adds label
labelText = StringVar()
labelText.set("Click Button")
label1 = Label(app, textvariable=labelText, height=4)
label1.pack()

#Creates a checkbox
checkBoxVal = IntVar()
checkBox1 =Checkbutton(app, variable=checkBoxVal, text= "Happy?")
checkBox1.pack()

#Creates a Input box
custName = StringVar(None)
yourName = Entry(app, textvariable =custName)
yourName.pack()

#Create Radiobutton
relStatus =StringVar()
relStatus.set(None)
radio1 = Radiobutton(app, text="Test1",value="Test1", variable = relStatus, command=beenClicked).pack()
radio1 = Radiobutton(app, text="Test2",value="Test2", variable = relStatus, command=beenClicked).pack()

#create a button
button1 = Button(app,text="Click Here", width = 20, command=changeLabel)
button1.pack(side='bottom',padx=15,pady=15)

app.mainloop()
