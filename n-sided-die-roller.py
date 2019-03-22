from random import randint
import tkinter
import tkinter.messagebox as tkMessageBox
from PIL import ImageTk , Image

class Application(tkinter.Frame):

    def __init__(self, root = None):
        super().__init__(root)
        self.root = root
        self.grid()
        self.setWidgets()

    def setWidgets(self):

        ## Roll Button
        self.rollButton = tkinter.Button(self.root,
                                    text = "Roll",
                                    command = lambda: self.executeRoll())
        self.rollButton.grid(row = 1, column = 0)

        ## Die Image Label
        self.dieImage = Image.open("d20.png")
        self.dieGraphic = ImageTk.PhotoImage(self.dieImage)
        self.dieLabel = tkinter.Label(self.root,
                                      image = self.dieGraphic)
        self.dieLabel.image = self.dieGraphic
        self.dieLabel.grid(row = 0, column = 0)

        ## Result Text Label
        self.resultLabel = tkinter.Label(self.root,
                                         text = "...",
                                         anchor = "center")
        self.resultLabel.grid(row = 0, column = 0)

    def executeRoll(self):
        result = randint(1,20)
        self.resultLabel.config(text = result)

tk = tkinter.Tk()
app = Application(root = tk)
app.mainloop()

print("Exiting program, have a nice day! :)")
