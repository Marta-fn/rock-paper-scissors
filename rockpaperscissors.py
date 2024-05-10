from tkinter import *
import customtkinter
import random
from PIL import Image
import instructionwindow

class RockPaperScissors(customtkinter.CTkToplevel):
  def __init__(self, parent):
    super().__init__(parent)

    self.title("Game: Rock, Paper, Scissor")
    window_width = 450
    window_height = 350
    screen_width = (self.winfo_screenwidth() // 2) - (window_width // 2)
    screen_height = (self.winfo_screenheight() // 2) - (window_height // 2)
    self.geometry(f"{window_width}x{window_height}+{screen_width}+{screen_height}")
    self.resizable(False,False)
    self.iconbitmap("4.ico")
    self.all_font = customtkinter.CTkFont(family="Roboto", size=16)

    self.choices = ["rock", "paper", "scissors"]
    self.user_points = 0
    self.computer_points = 0
    self.tie_points = 0

    self.text = StringVar() # for scoreboard

    self.rock_image = customtkinter.CTkImage(light_image=Image.open("5.png"),
                                             size=(100, 100))

    self.paper_image = customtkinter.CTkImage(light_image=Image.open("6.png"),
                                             size=(100, 100))
    self.scissors_image = customtkinter.CTkImage(light_image=Image.open("7.png"),
                                             size=(100, 100))
    self.createWidgets()

  def createWidgets(self):
    
    self.game_name = customtkinter.CTkLabel(self, 
                               text="Rock, Paper, Scissors",
                               font=self.all_font).grid(row=0, column=1, columnspan=3, pady=5)

    self.scoreboard = customtkinter.CTkLabel(self, 
                                textvariable=self.text,
                                font=self.all_font).grid(row=1, column=1, columnspan=3)
    
    self.insttruction = customtkinter.CTkLabel(self, 
                                  text="Pick an option:",
                                  font=self.all_font).grid(row=2, column=1, columnspan=3, pady=5)

    self.rock_button = customtkinter.CTkButton(self, 
                                  image=self.rock_image,
                                  text=None,
                                  fg_color="white",
                                  hover=False,
                                  cursor="hand2",
                                  font=self.all_font, 
                                  command=self.rock_picked).grid(row=3, column=1, padx=5)
    
    self.paper_button = customtkinter.CTkButton(self, 
                                   image=self.paper_image,
                                   text=None,
                                   fg_color="white",
                                   hover=False,   
                                   cursor="hand2",
                                   font=self.all_font,
                                   command=self.paper_picked).grid(row=3, column=2)
    
    self.scissor_button = customtkinter.CTkButton(self, 
                                     image=self.scissors_image, 
                                     text=None,
                                     fg_color="white",
                                     hover=False,  
                                     cursor="hand2",
                                     font=self.all_font,
                                     command=self.scissors_picked).grid(row=3, column=3, padx=5)

    self.instruction_button = customtkinter.CTkButton(self, 
                                         text="Instructions",
                                         cursor="hand2",
                                         font=self.all_font,
                                         command=self.open_instructions_window).grid(row=4, column=2, padx=5, pady=5)

    self.stop_button = customtkinter.CTkButton(self, 
                                  text="Stop Playing",
                                  font=self.all_font, 
                                  command=self.quit, 
                                  cursor="hand2").grid(row=4, columnspan=1, column=3, padx=5, pady=5)

  def rock_picked(self):
    self.computer_choice = random.choice(self.choices)
    if self.computer_choice == "paper":
        self.computer_points += 1
    elif self.computer_choice == "scissors":
      self.user_points += 1
    else:
      self.tie_points +=1
    
    self.show_scoreboard()
  
  def paper_picked(self):
    self.computer_choice = random.choice(self.choices)
    if self.computer_choice == "scissors":
        self.computer_points += 1
    elif self.computer_choice == "rock":
      self.user_points += 1
    else:
      self.tie_points +=1

    self.show_scoreboard()
  
  def scissors_picked(self):
    self.computer_choice = random.choice(self.choices)
    if self.computer_choice == "rock":
        self.computer_points += 1
    elif self.computer_choice == "paper":
      self.user_points += 1
    else:
      self.tie_points +=1

    self.show_scoreboard()
  
  def show_scoreboard(self):
      return self.text.set(f"Score:\nYou: {self.user_points}\nComputer: {self.computer_points}\nTies: {self.tie_points}")
  
  def open_instructions_window(self):
    window = instructionwindow.InstructionWindow(self)
    window.grab_set()
