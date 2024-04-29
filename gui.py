import tkinter as tk
from tkinter import *
from tkinter import ttk
import random

class RockPaperScissors(tk.Tk):
  def __init__(self):
    super().__init__()

    self.title("Game: Rock, Paper, Scissor")
    self.geometry("600x600")
    self.resizable(False,False)
    self.choices = ["rock", "paper", "scissors"]
    self.user_points = 0
    self.computer_points = 0
    self.tie_points = 0
    self.text = StringVar()

    self.createTabs()

  def createTabs(self):
    self.tab_parent = ttk.Notebook(self)

    self.game_tab = ttk.Frame(self.tab_parent)
    self.instruction_tab = ttk.Frame(self.tab_parent)
    self.tab_parent.add(self.game_tab, text ="Game") 
    self.tab_parent.add(self.instruction_tab, text ="Instructions") 
    self.tab_parent.pack(expand=1, fill="both")

    self.createFirstTabWidgets()
    self.createSecondTabWidgets()

  def createFirstTabWidgets(self):
    
    self.game_name = ttk.Label(self.game_tab, text="Rock, Paper, Scissors").grid(row=0, columnspan=3)

    self.scoreboard = ttk.Label(self.game_tab, textvariable=self.text).grid(row=1, columnspan=3)
    self.insttruction = ttk.Label(self.game_tab, text="Pick an option:").grid(row=2, columnspan=3)

    self.rock_button = ttk.Button(self.game_tab, text="Rock", cursor="hand2", command=self.rock_picked).grid(row=3, column=0, pady=5)
    self.paper_button = ttk.Button(self.game_tab, text="Paper", cursor="hand2", command=self.paper_picked).grid(row=3, column=1, pady=5)
    self.scissor_button = ttk.Button(self.game_tab, text="Scissors", cursor="hand2", command=self.scissors_picked).grid(row=3, column=3, pady=5)

    self.stop_button = ttk.Button(self.game_tab, text="Stop Playing", command=self.quit, cursor="hand2").grid(row=4, columnspan=3)

  def createSecondTabWidgets(self):

    self.insttructions = tk.Label(self.instruction_tab, text="""
                                  The player and the computer will select an option.\n
                                  Rock crushes scissors;\n
                                  Paper wraps rock;\n
                                  Scissors cut paper;\n 
                                  Ties occur when the choices are the same.""", justify="center").pack()

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