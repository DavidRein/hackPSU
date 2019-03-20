from random import randint
import tkinter
import tkinter.messagebox as tkMessageBox

print("##n-Sided Dice Roller##")

def executeRoll():
    tkMessageBox.showinfo("Result", randint(1,20))

root = tkinter.Tk()

rollButton = tkinter.Button(root, text = "Roll", command = lambda: executeRoll())

rollButton.pack()
root.mainloop()

print("Exiting program, have a nice day! :)")
