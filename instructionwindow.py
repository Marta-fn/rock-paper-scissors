import tkinter as tk
from tkinter import *
from tkinter import ttk

class InstructionWindow(tk.Toplevel):
  def __init__(self, parent):
    super().__init__(parent)

    self.title('Instructions')
    self.geometry('430x170')
    self.resizable(False,False)

    self.insttructions = ttk.Label(self, 
                                  text="The player and the computer will select an option.\nRock crushes scissors;\nPaper wraps rock;\nScissors cut paper;\nTies occur when the choices are the same.", 
                                  justify="center").pack(pady=10)

    ttk.Button(self,
            text='Close',
            command=self.destroy).pack(pady=5)