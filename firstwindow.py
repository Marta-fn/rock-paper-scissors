from tkinter import *
import customtkinter
import rockpaperscissors

class FirstWindow(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    self.title("Let's Play?")
    window_width = 450
    window_height = 350
    screen_width = (self.winfo_screenwidth() // 2) - (window_width // 2)
    screen_height = (self.winfo_screenheight() // 2) - (window_height // 2)
    self.geometry(f"{window_width}x{window_height}+{screen_width}+{screen_height}")
    self.resizable(False,False)
    self.iconbitmap("4.ico")
    self.all_font = customtkinter.CTkFont(family="Roboto", size=16)

    customtkinter.CTkLabel(self, 
                           text="Select the game you want to play: ", 
                           justify="center",
                           font=self.all_font).pack(pady=10)
    
    customtkinter.CTkButton(self,
                            text="Rock, Paper, Scissors",
                            font=self.all_font,
                            command=self.open_rock_paper_scissors, 
                            ).pack(pady=5)
    
    customtkinter.CTkButton(self,
                            text="Rock, Paper, Scissors, Lizard, Spock",
                            font=self.all_font, 
                            ).pack(pady=5)
    
    customtkinter.CTkButton(self,
                            text="I don't want to play",
                            font=self.all_font,
                            command=self.destroy 
                            ).pack(pady=5)

  def open_rock_paper_scissors(self):
    window = rockpaperscissors.RockPaperScissors(self)
    window.grab_set()
    app = FirstWindow()
    app.withdraw()

