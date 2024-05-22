from tkinter import *
import customtkinter
import random
from PIL import Image

class RockPaperScissorsLizardSpock(customtkinter.CTkToplevel):
  def __init__(self, parent):
    super().__init__(parent)

    self.title("Game: Rock, Paper, Scissor, Lizard, Spock")
    window_width = 450
    window_height = 350
    screen_width = (self.winfo_screenwidth() // 2) - (window_width // 2)
    screen_height = (self.winfo_screenheight() // 2) - (window_height // 2)
    self.geometry(f"{window_width}x{window_height}+{screen_width}+{screen_height}")
    self.resizable(False,False)
    self.iconbitmap("4.ico")
    self.all_font = customtkinter.CTkFont(family="Roboto", size=16)