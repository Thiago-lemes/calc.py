from tkinter import *
from tkinter import *
from tkinter import ttk
from turtle import color, width 

color1 = "#060021"
window = Tk()
window.title("Calculadora")
#geometry vai defenir o tamanha da calculadora( largura e altura)
window.geometry("240x318")
window.config(bg = color1)

frame_tela = Frame(window, width= 240, height = 50, )
frame_tela.grid(row = 30, column = 30)

window.mainloop()