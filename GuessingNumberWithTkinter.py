import random
from tkinter import *

WIN = Tk()
WIDTH = 400
HEIGHT = 400
WIN.geometry("400x400")
WIN.title("Guessing Number")



class Random :
    FirstNumber = IntVar()
    SecondNumber = IntVar()
    GuessedNumber = IntVar()
    value = 0
    Result = 0
    def Guessing_Number(self):
        if self.FirstNumber.get() == 0 and self.SecondNumber.get() ==0 and self.GuessedNumber.get() == 0:
            self.Result.configure(text = "Please Enter All The Columns...")
        else:
            self.value = random.randint(self.FirstNumber.get() , self.SecondNumber.get())
            if self.value == self.GuessedNumber.get():
                self.Result.configure(text = "Hurry You Own..:)", fg = "Green")
            elif self.value < self.GuessedNumber.get():
                self.Result.configure(text = "You'r Guessed Number Is Greater Than Guessing Number ")
            else:
                self.Result.configure(text = "You'r Guessed Number Is Less Than Guessing Number ")
           
     def __init__(self):
       
        L1 = Label(WIN, text = "<-----Guessing Number--->", fg="white", bg="black", font=("arial",13))
        L1.grid(row=0, column=WIDTH//2 , padx=5, pady=5)

        #creating Labels
        self.Lfont = ("arial", 10)
        self.L2 = Label(WIN, text = "Enter You'r First Number:",fg = "red", font=self.Lfont)
        self.L2.grid(row=2, column=2 , padx=5, pady=5)
        self.E1 = Entry(WIN, textvariable=self.FirstNumber)
        self.E1.grid(row=2, column=6 , padx=5, pady=5)

        self.L3 = Label(WIN, text = "Enter You'r Second Number:",fg = "red", font=self.Lfont)
        self.L3.grid(row=4, column=2 , padx=5, pady=5)
        E2 = Entry(WIN, textvariable=self.SecondNumber)
        E2.grid(row=4, column=6 , padx=5, pady=5)

        self.L4 = Label(WIN, text = "Enter You'r Guessing Number:",fg = "red", font=self.Lfont)
        self.L4.grid(row=6, column=2 , padx=5, pady=5)
        self.E3 = Entry(WIN, textvariable=self.GuessedNumber)
        self.E3.grid(row=6, column=6 , padx=5, pady=5)

        self.btn = Button(WIN, text = "Check",fg= "blue", command=self.Guessing_Number)
        self.btn.grid(row=8, column=5 , padx=5, pady=5)

        self.Result = Label(WIN, text = "Result",fg = "red", font=self.Lfont)
        self.Result.grid(row=12, column=5 ,columnspan =2, padx=5, pady=5)

        WIN.mainloop()
        
Gnumber = Random()
        
        
