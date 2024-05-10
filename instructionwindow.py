from tkinter import *
import customtkinter

class InstructionWindow(customtkinter.CTkToplevel):
  def __init__(self, parent):
    super().__init__(parent)

    self.title('Instructions')
    window_width = 430
    window_height = 170
    screen_width = (self.winfo_screenwidth() // 2) - (window_width // 2)
    screen_height = (self.winfo_screenheight() // 2) - (window_height // 2)
    self.geometry(f"{window_width}x{window_height}+{screen_width}+{screen_height}")
    self.resizable(False,False)

    customtkinter.CTkLabel(self, 
                           text="The player and the computer will select an option.\nRock crushes scissors;\nPaper wraps rock;\nScissors cut paper;\nTies occur when the choices are the same.", 
                           justify="center",
                           font=parent.all_font).pack(pady=10)

    customtkinter.CTkButton(self,
            text='Close',
            font=parent.all_font,
            command=self.destroy).pack(pady=5)