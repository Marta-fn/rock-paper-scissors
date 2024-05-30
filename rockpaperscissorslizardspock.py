from tkinter import *
import customtkinter
import random
from PIL import Image

class RockPaperScissorsLizardSpock(customtkinter.CTkToplevel):
  def __init__(self, parent):
    super().__init__(parent)

    self.title("Game: Rock, Paper, Scissor, Lizard, Spock")
    window_width = 470
    window_height = 350
    screen_width = (self.winfo_screenwidth() // 2) - (window_width // 2)
    screen_height = (self.winfo_screenheight() // 2) - (window_height // 2)
    self.geometry(f"{window_width}x{window_height}+{screen_width}+{screen_height}")
    self.resizable(False,False)
    self.iconbitmap("4.ico")
    self.all_font = customtkinter.CTkFont(family="Roboto", size=16)

    self.choices = ["rock", "paper", "scissors", "lizard", "spock"]
    self.user_points = 0
    self.computer_points = 0
    self.tie_points = 0
    self.winner = 0

    self.text = StringVar() # for scoreboard
    self.choicesText = StringVar() #for choices
    self.winnerText = StringVar()

    self.createWidgets()

  def createWidgets(self):
    
    self.game_name = customtkinter.CTkLabel(self, 
                               text="Rock, Paper, Scissors, Lizard, Spock",
                               font=customtkinter.CTkFont(family="Roboto", size=20)).grid(row=0, column=1, columnspan=3, pady=15)

    self.both_choices = customtkinter.CTkLabel(self, 
                                textvariable=self.choicesText,
                                font=self.all_font).grid(row=1, column=1, columnspan=1)
    
    self.winner_label = customtkinter.CTkLabel(self,
                                         textvariable=self.winnerText, 
                                         width=100,
                                         height=100,
                                         font=customtkinter.CTkFont(family="Roboto", size=20))
    self.winner_label.grid(row=1, column=2, columnspan=1)
    
    self.scoreboard = customtkinter.CTkLabel(self, 
                                textvariable=self.text,
                                font=self.all_font).grid(row=1, column=3, columnspan=1)
    
    self.insttruction = customtkinter.CTkLabel(self, 
                                  text="Pick an option:",
                                  font=self.all_font).grid(row=2, column=1, columnspan=3, pady=5)

    self.rock_button = customtkinter.CTkButton(self, 
                                  text="Rock",
                                  fg_color="white",
                                  hover=False,
                                  cursor="hand2",
                                  font=self.all_font, 
                                  command=self.rock_picked).grid(row=3, column=1, padx=10)
    
    self.paper_button = customtkinter.CTkButton(self,
                                   text="Paper",
                                   fg_color="white",
                                   hover=False,   
                                   cursor="hand2",
                                   font=self.all_font,
                                   command=self.paper_picked).grid(row=3, column=2)
    
    self.scissor_button = customtkinter.CTkButton(self,
                                     text="Scissor",
                                     fg_color="white",
                                     hover=False,  
                                     cursor="hand2",
                                     font=self.all_font,
                                     command=self.scissors_picked).grid(row=3, column=3, padx=10)
    
    self.lizard_button = customtkinter.CTkButton(self,
                                     text="Lizard",
                                     fg_color="white",
                                     hover=False,
                                     cursor="hand2",
                                     font=self.all_font,
                                     command=self.lizard_picked).grid(row=4, column=1)
    
    self.spock_button = customtkinter.CTkButton(self,
                                     text="Spock",
                                     fg_color="white",
                                     hover=False,
                                     cursor="hand2",
                                     font=self.all_font,
                                     command=self.spock_picked).grid(row=4, column=2, pady=5)

    self.instruction_button = customtkinter.CTkButton(self, 
                                         text="Instructions",
                                         cursor="hand2",
                                         font=self.all_font,
                                         height=45,
                                         command=self.open_instructions_window).grid(row=5, column=2, padx=5, pady=15)

    self.stop_button = customtkinter.CTkButton(self, 
                                  text="Stop Playing",
                                  font=self.all_font,
                                  fg_color="#de3c4b",
                                  hover_color="#932833",
                                  height=45, 
                                  command=self.destroy, 
                                  cursor="hand2").grid(row=5, columnspan=1, column=3, padx=5, pady=15)

  def rock_picked(self):
    self.user_choice = "Rock"
    self.computer_choice = random.choice(self.choices)
    if self.computer_choice == "paper" or self.computer_choice == "spock":
        self.computer_points += 1
        self.winner = "Computer"
    elif self.computer_choice == "scissors" or self.computer_choice == "lizard":
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
    if self.computer_choice == "scissors" or self.computer_choice == "lizard":
        self.computer_points += 1
        self.winner = "Computer"
    elif self.computer_choice == "rock" or self.computer_choice == "spock":
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
    if self.computer_choice == "rock" or self.computer_choice == "spock":
        self.computer_points += 1
        self.winner = "Computer"
    elif self.computer_choice == "paper" or self.computer_choice == "lizard":
      self.user_points += 1
      self.winner = "You"
    else:
      self.tie_points +=1
      self.winner = 0

    self.show_choices()
    self.show_winner()
    self.show_scoreboard()

  def lizard_picked(self):
    self.user_choice = "Lizard"
    self.computer_choice = random.choice(self.choices)
    if self.computer_choice == "rock" or self.computer_choice == "scissors":
        self.computer_points += 1
        self.winner = "Computer"
    elif self.computer_choice == "paper" or self.computer_choice == "spock":
      self.user_points += 1
      self.winner = "You"
    else:
      self.tie_points +=1
      self.winner = 0

    self.show_choices()
    self.show_winner()
    self.show_scoreboard()

  def spock_picked(self):
    self.user_choice = "Spock"
    self.computer_choice = random.choice(self.choices)
    if self.computer_choice == "paper" or self.computer_choice == "lizard":
        self.computer_points += 1
        self.winner = "Computer"
    elif self.computer_choice == "scisors" or self.computer_choice == "rock":
      self.user_points += 1
      self.winner = "You"
    else:
      self.tie_points +=1
      self.winner = 0

    self.show_choices()
    self.show_winner()
    self.show_scoreboard()

  def show_scoreboard(self):
      return self.text.set(f"Score:\n\nYou: {self.user_points}\nComputer: {self.computer_points}\nTies: {self.tie_points}")
  
  def show_choices(self):
    return self.choicesText.set(f"Computer picked:\n{(self.computer_choice).capitalize()}\n\nYou picked:\n{self.user_choice}")
  
  def change_text_color(self):
    if self.winner == "Computer":
      return "#de3c4b"
    elif self.winner == "You":
      return "#7fb069"
    else:
      return "black"

  def show_winner(self):
    self.winner_label.configure(text_color=self.change_text_color())

    if self.winner == "Computer":
      return self.winnerText.set("Computer\nWins!")
    elif self.winner == "You":
      return self.winnerText.set("You\nWin!")
    else:
      return self.winnerText.set("Its a tie.") 

  
  def open_instructions_window(self):
    window = instructionwindow.InstructionWindow(self)
    window.grab_set()
