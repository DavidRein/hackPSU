from random import randint
import tkinter
import tkinter.messagebox as tkMessageBox

print("##n-Sided Dice Roller##")
class Application(tkinter.Frame):

    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.setWidgets()

    def setWidgets(self):
        self.rollButton = tkinter.Button(self.root,
                                    text = "Roll",
                                    command = lambda: self.executeRoll())
        self.rollButton.pack()

    def executeRoll(self):
        tkMessageBox.showinfo("Result", randint(1,20))

tk = tkinter.Tk()
app = Application(root = tk)
app.mainloop()

print("Exiting program, have a nice day! :)")
