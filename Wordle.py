from cProfile import label
from tkinter import *
from tkinter.ttk import Entry
from tkinter import messagebox

import words

# from PycharmProjects.pythonProject1.words import getword


w = Tk()
w.title("GIRDEL")
w.geometry('700x700')
w.config(bg="white")
b = words.getword()

green = "#02f543"
yellow = "#e9f502"
grey = "#60635e"
guessnum = 1
e  =  Entry(w)
e.grid(row = 999 , column = 0,padx = 10 , pady=10,columnspan = 5)

def getguess():
    global b
    global guessnum
    guessnum +=1
    guess = e.get().lower()
    e.delete(0,END)


    if len(guess) == 6 :
        if b == guess:
            messagebox.showinfo("CONGRATULATIONS!! YOU WON")
            return
        else :
            for i, letter in  enumerate(guess) :
                label1 = Label(w,text=letter.upper())
                label1.grid(row=0 , column = i,padx=10,pady=10)

                if letter==b[i]:
                    label1.config(bg=green,fg="black")

                if letter in b and not letter == b[i]:
                    label1.config(bg=yellow,fg="black")

                if letter not in b :
                    label1.config(bg=grey,fg="black")

    else :
        messagebox.showinfo("please type 6 letter word")

bn = Button(w,text="guess",command=getguess)
bn.grid(row=999,column=3,columnspan=3)
print (b)
w.mainloop()