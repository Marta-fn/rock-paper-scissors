import tkinter as tk
from tkinter import *
from tkinter import ttk

class InstructionWindow(tk.Toplevel):
  def __init__(self, parent):
    super().__init__(parent)

    self.title('Instructions')
    window_width = 430
    window_height = 170
    screen_width = (self.winfo_screenwidth() // 2) - (window_width // 2)
    screen_height = (self.winfo_screenheight() // 2) - (window_height // 2)
    self.geometry(f"{window_width}x{window_height}+{screen_width}+{screen_height}")
    self.resizable(False,False)

    self.insttructions = ttk.Label(self, 
                                  text="The player and the computer will select an option.\nRock crushes scissors;\nPaper wraps rock;\nScissors cut paper;\nTies occur when the choices are the same.", 
                                  justify="center").pack(pady=10)

    ttk.Button(self,
            text='Close',
            padding=5,
            command=self.destroy).pack(pady=5)