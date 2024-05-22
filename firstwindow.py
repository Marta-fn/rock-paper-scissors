from tkinter import *
import customtkinter
import rockpaperscissors
import rockpaperscissorslizardspock

class FirstWindow(customtkinter.CTk):
  def __init__(self):
    super().__init__()

    self.title("Let's Play?")
    window_width = 370
    window_height = 200
    screen_width = (self.winfo_screenwidth() // 2) - (window_width // 2)
    screen_height = (self.winfo_screenheight() // 2) - (window_height // 2)
    self.geometry(f"{window_width}x{window_height}+{screen_width}+{screen_height}")
    self.resizable(False,False)
    self.iconbitmap("4.ico")
    self.all_font = customtkinter.CTkFont(family="Roboto", size=16)

    customtkinter.CTkLabel(self, 
                           text="Select the game you want to play: ", 
                           justify="center",
                           font=self.all_font).grid(row=0, column=1, columnspan=2, pady=10)
    
    customtkinter.CTkButton(self,
                            text="Rock, Paper, Scissors",
                            font=self.all_font,
                            height=50,
                            width=50, 
                            fg_color="#7fb069",
                            hover_color="#386150",
                            cursor="hand2", 
                            command=self.open_rock_paper_scissors, 
                            ).grid(row=1, column=1, pady=5, padx=10)
    
    customtkinter.CTkButton(self,
                            text="Rock, Paper, Scissors,\n Lizard, Spock",
                            font=self.all_font,
                            height=50,
                            width=50,
                            fg_color="#7fb069",
                            hover_color="#386150", 
                            cursor="hand2",
                            command=self.open_rock_paper_scissors_lizard_spock, 
                            ).grid(row=1, column=2, pady=5, padx=10)

    customtkinter.CTkButton(self,
                            text="I don't want to play",
                            font=self.all_font,
                            height=50,
                            width=50, 
                            command=self.destroy,
                            fg_color="#de3c4b",
                            hover_color="#932833",
                            cursor="hand2", 
                            ).grid(row=2, column=1, columnspan=2, pady=15)

  def open_rock_paper_scissors(self):
    window = rockpaperscissors.RockPaperScissors(self)
    window.grab_set()
    # app = FirstWindow()
    # app.withdraw()
  
  def open_rock_paper_scissors_lizard_spock(self):
    window = rockpaperscissorslizardspock.RockPaperScissorsLizardSpock(self)
    window.grab_set()
    # app = FirstWindow()
    # app.withdraw()
