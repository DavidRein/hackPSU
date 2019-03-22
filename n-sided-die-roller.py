from random import randint
import tkinter
import tkinter.messagebox as tkMessageBox
from PIL import ImageTk , Image

print("##n-Sided Dice Roller##")
class Application(tkinter.Frame):

    def __init__(self, root = None):
        super().__init__(root)
        self.result = 0
        self.root = root
        self.pack()
        self.setWidgets()

    def setWidgets(self):
        self.rollButton = tkinter.Button(self.root,
                                    text = "Roll",
                                    command = lambda: self.executeRoll())
        self.rollButton.pack()

        self.dieImage = Image.open("d20.png")
        self.dieGraphic = ImageTk.PhotoImage(self.dieImage)
        self.dieLabel = tkinter.Label(self.root,
                                      image = self.dieGraphic)
        self.dieLabel.image = self.dieGraphic
        self.dieLabel.pack()

        self.resultLabel = tkinter.Label(self.root,
                                         text = str(self.result),
                                         anchor = "center")
        self.resultLabel.pack()

    def executeRoll(self):
        self.result = randint(1,20)
        self.resultLabel.config(text = self.result)
        print("updating roll..." , self.result)

tk = tkinter.Tk()
app = Application(root = tk)
app.mainloop()

print("Exiting program, have a nice day! :)")
