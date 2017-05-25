from tkinter import *
from tkinter import messagebox
from subprocess import Popen
import builtins
import Game
import sys


mGui = Tk()
screen_width = mGui.winfo_screenwidth()
screen_height = mGui.winfo_screenheight()

mGui.geometry('250x157+0+500')
mGui.title('Autonomous Treasure Hunt')

w = 60


def main():

    def runreport():
        Popen(['SE733.pdf'], shell=True)


    def runrules():
        Popen(['Rules.pdf'], shell=True)


    def buttonpress():
        d = dim.get()
        r = rock.get()
        f = fire.get()
        l = reward.get()
        dis = discount.get()
        if d < 5 or d > 10:
            messagebox.showinfo(title = 'Dimension Error', message = 'Grid is nxn and 5 < n < 10')
        elif (r+f) > (d-1):
            messagebox.showinfo(title = 'Fire and Rock Sum Error', message = '#Fires + #Rocks must be =< n! Please reconsider...')
        elif l > 0:
            messagebox.showinfo(title = 'Living Reward Error', message = 'Living Reward must be =< 0! Please reconsider...')
        elif dis < 0 or dis > 1:
            messagebox.showinfo(title='Discount Rate Error', message='Discount Rate must be between 0 and 1! Please reconsider...')
        else:
            messagebox.showinfo(title = 'Placement method', message = 'INSTRUCTIONS:\n i) Place your treasure, all your rocks then all your fires by consecutive mouse clicks ORDINALLY!\n ii) Click each square only once\n iii) Restart by closeing the game board\n iv) Close GUI to exit the program ')
            Game.game(d, r, f, w, l, dis)

    dim = IntVar()
    rock = IntVar()
    fire = IntVar()
    reward = DoubleVar()
    discount = DoubleVar()

    menubar = Menu(mGui)
    helpmenu = Menu(menubar, tearoff = 0)
    helpmenu.add_command(label = 'Rules', command = runrules)
    helpmenu.add_command(label = 'Report', command = runreport)
    menubar.add_cascade(label = 'Help', menu = helpmenu)
    mGui.config(menu = menubar)

    lab1 = Label(text = 'Square Grid n = ', fg = 'blue').grid(row = 0, column = 0, sticky = E)
    lab2 = Label(text = 'Number of Rocks = ', fg = 'blue').grid(row = 1, column = 0, sticky = E)
    lab3 = Label(text = 'Number of Fires = ', fg = 'blue').grid(row = 2, column = 0, sticky = E)
    lab4 = Label(text = 'Living Reward = ', fg = 'blue').grid(row = 3, column = 0, sticky = E)
    lab5 = Label(text = 'Discount Rate = ', fg = 'blue').grid(row = 4, column = 0, sticky = E)

    ent1 = Entry(mGui, textvariable = dim, width = 2). place(x = 110, y = 1)
    ent2 = Entry(mGui, textvariable = rock, width = 2). place(x = 110, y = 23)
    ent3 = Entry(mGui, textvariable = fire, width = 2). place(x = 110, y = 45)
    ent4 = Entry(mGui, textvariable = reward, width = 2). place(x = 110, y = 66)
    ent5 = Entry(mGui, textvariable = discount, width = 2). place(x = 110, y = 87)

    mbutton = Button(mGui, text='Proceed to Placement!', command = buttonpress, fg='black', bg='green')
    mbutton.place(x=110, y= 122)
    mGui.mainloop()