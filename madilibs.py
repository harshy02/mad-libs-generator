#using tkinter for python GUI
#user input is taken in terminal

from tkinter import *

#initialize window using tkinter
root = Tk()
root.geometry('300x300')
root.title('Funny fill-in')
Label(root, text = 'Fill-Up & Have fun!!!', font = 'arial 20 bold', justify = 'center').pack()
Label(root, text = 'Pick one:', font = 'arial 15 bold', justify = 'center').place(x = 40, y = 50)

#defining function to display output
def printOutput(output):
    label = Label(root, text = output, font = 'arial 15', wraplength=250, justify = 'center').place(x = 40, y = 200)
    
#defining functions for each madlib separately
def madlib1():
    adj1 = input('Enter an adjective: ')
    adj2 = input('Enter an adjective: ')
    adj3 = input('Enter an adjective: ')

    #string concatenation
    text = f"All the things I really like are either {adj1}, {adj2} or {adj3}."
    
    printOutput(text)

def madlib2():
    noun1 = input('Enter a noun: ')
    noun2 = input('Enter a noun: ')
    verb = input("Enter a verb with -ing: ")
    noun3 = input('Enter a noun: ')
    text = f"I like to think of {noun1} less like a {noun2} and more like a {verb} {noun3}."

    printOutput(text)

def madlib3():
    noun = input("Enter a noun: ")
    food1 = input("Enter a food item: ")
    food2 = input("Enter a food item: ")
    adj = input("Enter an adjective: ")
    text = f"{noun} are like {food1} - mostly {adj} with a few {food2}"
    
    printOutput(text)

#initializing buttons for madlib selection
Button(root, text = 'one', font = 'arial 15', command = madlib1, bg = 'ghost white').place(x=40, y=80)
Button(root, text = 'two', font = 'arial 15', command = madlib2, bg = 'ghost white').place(x=40, y=120)
Button(root, text = 'three', font = 'arial 15', command = madlib3, bg = 'ghost white').place(x=40, y=160)

root.mainloop()

