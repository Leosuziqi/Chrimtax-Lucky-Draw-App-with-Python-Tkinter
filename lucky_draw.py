import tkinter

import keyboard as keyboard
import numpy as np
import random
from tkinter import Tk, mainloop,TOP
from tkinter.ttk import Button
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import pickle
import pygame
import keyboard

size_result = 100

#Main Window
root = Tk()

root.title('Christmas Dinner ')

#refresh()

#w = bg.width()
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
#h = bg.height()

## set background and Text
root.overrideredirect(True)
root.configure(background='white')
image = Image.open('cxtree.jpg')
new_image = image.resize((int(w*4/5), h))
bg = ImageTk.PhotoImage(new_image)

root.geometry('%dx%d' % (w,h))
label = Label(root,image=bg)
label.place(x=0,y=0)

Header = tkinter.Label(root, text="Winner: ")
Header.config(font=("Courier", 50))
root.overrideredirect(True)
Header.place(relx=0.9, rely=0.05, anchor="center")

# Entry for guest_number and prize_number
guest_number_label=tkinter.Label(root, text="# of Guests: ",font=("Ariel", int(30*w/1536),"bold"), bg="red")
guest_number_label.place(relx=0.1, rely=0.35, anchor="s")
guest_number_entry=tkinter.Entry(root,font=("Ariel", int(30*w/1536),"bold"), width=5)
guest_number_entry.place(relx=0.1, rely=0.35, anchor="n")

count = 0.1

#Command when Click Start
def refresh(event):
    qty = guest_number
    global count
    
    #Generate a random value
    number_new = random.randint(88208, 88208 + qty)
    num_str=str(0) + str(number_new)+'\n'

    #check redundency
    file1 = open('Winner_List.txt', 'r')
    list1 = file1.readlines()
    print(list1)

    while num_str in list1:
        print(num_str)
        print("re")
        number_new = random.randint(88208, 88208 + qty)
        num_str = str(0) + str(number_new) + '\n'
        
    #    number = random.randint(88208, 88208 + qty)
    result = str(0) + str(number_new)
    output = result + '\n'


    #save to .txt
    f = open('Winner_List.txt', 'a')  # w : writing mode  /  r : reading mode  /  a  :  appending mode
    f.write('{}'.format(output))
    f.close()

    #Display Result
    winnter = tkinter.Label(root, text=result)
    winnter.config(font=("Courier", 60))
    winnter.place(relx=0.9, rely=0.05+count, anchor="center")
    count=count+0.09
    
# Start Buttom
button_1 = Button(root, text="START",font=("Courier", 50),bg= 'grey',activebackground='green')
button_1.place(relx=0.4, rely=0.75, anchor="center")
button_1.bind("<Button-1>", refresh)
root.bind("<Return>")
root.bind("<Return>", refresh)

## adding bg music
url = "Jingle-Bells-3.mp3"
pygame.mixer.init()
m = pygame.mixer.music.load(url)
pygame.mixer.music.play()



root.mainloop()
