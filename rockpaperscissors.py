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
    window_height = 400
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
    self.winner = 0

    self.text = StringVar() # for scoreboard
    self.choicesText = StringVar() #for choices
    self.winnerText = StringVar()

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
                               font=self.all_font).grid(row=0, column=1, columnspan=3, pady=10)

    self.bothChoices = customtkinter.CTkLabel(self, 
                                textvariable=self.choicesText,
                                font=self.all_font).grid(row=1, column=1, columnspan=1)
    
    self.winner = customtkinter.CTkLabel(self, 
                                textvariable=self.winnerText,
                                bg_color=self.change_bg_color(),
                                width=100,
                                height=100,
                                font=self.all_font).grid(row=1, column=2, columnspan=1)
    
    self.scoreboard = customtkinter.CTkLabel(self, 
                                textvariable=self.text,
                                font=self.all_font).grid(row=1, column=3, columnspan=1)
    
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
                                         command=self.open_instructions_window).grid(row=4, column=2, padx=5, pady=10)

    self.stop_button = customtkinter.CTkButton(self, 
                                  text="Stop Playing",
                                  font=self.all_font,
                                  fg_color="#de3c4b",
                                  hover_color="#932833", 
                                  command=self.destroy, 
                                  cursor="hand2").grid(row=4, columnspan=1, column=3, padx=5, pady=10)

  def rock_picked(self):
    self.user_choice = "Rock"
    self.computer_choice = random.choice(self.choices)
    if self.computer_choice == "paper":
        self.computer_points += 1
        self.winner = "Computer"
    elif self.computer_choice == "scissors":
      self.user_points += 1
      self.winner = "You"
    else:
      self.tie_points +=1
      self.winner = 0
    
    self.show_choices()
    self.show_winner()
    self.show_scoreboard()
  
  def paper_picked(self):
    self.user_choice = "Paper"
    self.computer_choice = random.choice(self.choices)
    if self.computer_choice == "scissors":
        self.computer_points += 1
        self.winner = "Computer"
    elif self.computer_choice == "rock":
      self.user_points += 1
      self.winner = "You"
    else:
      self.tie_points +=1
      self.winner = 0

    self.show_choices()
    self.show_winner()
    self.show_scoreboard()
  
  def scissors_picked(self):
    self.user_choice = "Scissors"
    self.computer_choice = random.choice(self.choices)
    if self.computer_choice == "rock":
        self.computer_points += 1
        self.winner = "Computer"
    elif self.computer_choice == "paper":
      self.user_points += 1
      self.winner = "You"
    else:
      self.tie_points +=1
      self.winner = 0

    self.show_choices()
    self.show_winner()
    self.show_scoreboard()
  
  def show_scoreboard(self):
      return self.text.set(f"Score:\nYou: {self.user_points}\nComputer: {self.computer_points}\nTies: {self.tie_points}")
  
  def show_choices(self):
    return self.choicesText.set(f"Computer picked:\n{(self.computer_choice).capitalize()}\n\nVS\n\n You picked:\n{self.user_choice}")
  
  def change_bg_color(self):
    if self.winner == "Computer":
      return "#e77a85"
    elif self.winner == "You":
      return "#bce3ab"
    else:
      return "transparent"

  def show_winner(self):
    if self.winner == "Computer":
      return self.winnerText.set("Computer\nWins!")
    elif self.winner == "You":
      return self.winnerText.set("You\nWin!")
    else:
      return self.winnerText.set("Its a tie.")
  
  def open_instructions_window(self):
    window = instructionwindow.InstructionWindow(self)
    window.grab_set()
