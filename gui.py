import tkinter as tk
from tkinter import *
from tkinter import ttk
import random
import instructionwindow

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
    all_font = ttk.Style()
    all_font.configure(".", font=("Roboto", 12))

    self.createWidgets()

  def createWidgets(self):
    
    self.game_name = ttk.Label(self, 
                               text="Rock, Paper, Scissors").grid(row=0, column=1, columnspan=3, pady=5)

    self.scoreboard = ttk.Label(self, 
                                textvariable=self.text).grid(row=1, column=1, columnspan=3)
    
    self.insttruction = ttk.Label(self, 
                                  text="Pick an option:").grid(row=2, column=1, columnspan=3, pady=5)

    self.rock_button = ttk.Button(self, 
                                  text="Rock", 
                                  cursor="hand2", 
                                  command=self.rock_picked).grid(row=3, column=1, padx=5)
    
    self.paper_button = ttk.Button(self, 
                                   text="Paper", 
                                   cursor="hand2", 
                                   command=self.paper_picked).grid(row=3, column=2)
    
    self.scissor_button = ttk.Button(self, 
                                     text="Scissors", 
                                     cursor="hand2", 
                                     command=self.scissors_picked).grid(row=3, column=3, padx=5)

    self.instruction_button = ttk.Button(self, 
                                         text="Instructions",
                                         cursor="hand2",
                                         command=self.open_instructions_window).grid(row=4, column=2, padx=5, pady=5)

    self.stop_button = ttk.Button(self, 
                                  text="Stop Playing", 
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