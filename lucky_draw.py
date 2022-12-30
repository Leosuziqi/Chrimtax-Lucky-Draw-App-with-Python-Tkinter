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
    
    # gif display
    for openImage_frames in ImageSequence.Iterator(openImage):
        openImage_resized = openImage_frames.resize((int(w*1/5), int(h*(1/5))))
        openImage_show = ImageTk.PhotoImage(openImage_resized)
        gif_Label1 = Label(root)
        gif_Label2 = Label(root)
        gif_Label1.place(relx=0.15, rely=0.75, anchor="center")
        gif_Label1.config(image=openImage_show)

        gif_Label2.place(relx=0.65, rely=0.75, anchor="center")
        gif_Label2.config(image=openImage_show)
        root.update()
        time.sleep(0.06)

    gif_idle1 = Label(root,image=bg_idle)
    gif_idle1.place(relx=0.15, rely=0.75, anchor="center")
    gif_idle2 = Label(root,image=bg_idle)
    gif_idle2.place(relx=0.65, rely=0.75, anchor="center")
    
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

    # save to history_log.txt
    f = open('history_log.txt', 'a')  # w : writing mode  /  r : reading mode  /  a  :  appending mode
    f.write('{}'.format(output))
    f.close()
    
    #Display Result
    shown = '#' + str(prize_amount)+': ' +result
    winnter = tkinter.Label(root, text=shown)
    winnter.config(font=("Courier", 60))
    winnter.place(relx=0.9, rely=0.05+count, anchor="center")
    count=count+0.09
    
# Start Buttom
button_1 = Button(root, text="START",font=("Courier", 50),bg= 'grey',activebackground='green')
button_1.place(relx=0.4, rely=0.75, anchor="center")
button_1.bind("<Button-1>", refresh)
root.bind("<Return>")
root.bind("<Return>", refresh)

def retrial(event):
    retrial_file2 = open('Winner_List.txt', 'r')
    retrial_list2 = retrial_file2.readlines()
    retrial_list2_undo=retrial_list2[0:len(retrial_list2)-1]
    #print(retrial_list2_undo)
    retrial_file2.close()
    os.remove("Winner_List.txt")


    with open(r'Winner_List.txt', 'w') as fp2:
        for item2 in retrial_list2_undo:
            # write each item on a new line
            fp2.write(item2)
    fp2.close()

    refresh(event)
    
#Re_draw
button_2 = Button(root, text="Re-Draw",font=("Ariel", int(35*w/1536)),bg= 'grey',activebackground='green')
button_2.place(relx=0.4, rely=0.9, anchor="center")
button_2.bind("<Button-1>", retrial)
root.bind("<Shift_R >")
root.bind("<Shift_R >",retrial)

## adding bg music
url = "Jingle-Bells-3.mp3"
pygame.mixer.init()
m = pygame.mixer.music.load(url)
pygame.mixer.music.play()



root.mainloop()
