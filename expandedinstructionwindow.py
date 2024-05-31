from tkinter import *
import customtkinter

class ExpandedInstructionWindow(customtkinter.CTkToplevel):
  def __init__(self, parent):
    super().__init__(parent)

    self.title('Instructions')
    window_width = 430
    window_height = 260
    screen_width = (self.winfo_screenwidth() // 2) - (window_width // 2)
    screen_height = (self.winfo_screenheight() // 2) - (window_height // 2)
    self.geometry(f"{window_width}x{window_height}+{screen_width}+{screen_height}")
    self.resizable(False,False)

    customtkinter.CTkLabel(self, 
                           text="Scissors cuts Paper\nPaper covers Rock\nRock crushes Lizard\nLizard poisons Spock\nSpock smashes Scissors\nScissors decapitates Lizard\nLizard eats Paper\nPaper disproves Spock\nSpock vaporizes Rock\nRock crushes Scissors",
                           anchor="center",
                           font=parent.all_font).pack(pady=10)

    customtkinter.CTkButton(self,
            text='Close',
            font=parent.all_font,
            fg_color="#de3c4b",
            hover_color="#932833",
            command=self.destroy).pack(pady=5)