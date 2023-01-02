import tkinter
import numpy as np
import random
from tkinter import *
from PIL import ImageTk, Image
import pygame
import keyboard
import time
from PIL import Image, ImageSequence

# Parameters
guest_number = 100
prize_number = 51
global prize_amount
global openImage_resized


def display_GIF(openImage):
    #display frame by frame
    for openImage_frames in ImageSequence.Iterator(openImage):
        openImage_resized = openImage_frames.resize((400, 300))
        openImage_show = ImageTk.PhotoImage(openImage_resized)
        gif_Label1 = Label(root)
        gif_Label2 = Label(root)

        #GIFs Location
        gif_Label1.place(relx=0.15, rely=0.75, anchor="center")
        gif_Label1.config(image=openImage_show)

        gif_Label2.place(relx=0.65, rely=0.75, anchor="center")
        gif_Label2.config(image=openImage_show)
        root.update()
        #display speed
        time.sleep(0.06)


def output_to_txt(output):
    output_display = '#' + str(prize_amount) + ': ' + output
    f = open('Winner_List.xlsx', 'a')  # w : writing mode  /  r : reading mode  /  a  :  appending mode
    f.write('{}'.format(output_display))
    f.close()

    # save to history_log.txt
    f = open('history_log.txt', 'a')  # w : writing mode  /  r : reading mode  /  a  :  appending mode
    f.write('{}'.format(output))
    f.close()

def generate_random(list1):
    qty = guest_number

    number_new = random.randint(88208, 88208 + qty)
    num_str = str(0) + str(number_new) + '\n'

    while num_str in list1:
        number_new = random.randint(88208, 88208 + qty)
        num_str = str(0) + str(number_new) + '\n'
        # print(num_str)

    return number_new


def refresh(event):
    guest_number=int(guest_number_entry.get())
    # gif display
    display_GIF(openImage)

    # GIFs idle state
    gif_idle1 = Label(root, image=bg_idle)
    gif_idle1.place(relx=0.15, rely=0.75, anchor="center")
    gif_idle2 = Label(root, image=bg_idle)
    gif_idle2.place(relx=0.65, rely=0.75, anchor="center")

    # check redundency
    file1 = open('history_log.txt', 'r')
    list1 = file1.readlines()
    print(len(list1))
    prize_amount = prize_number - len(list1);

    # Check if drawer is empty
    count = 0.1
    if prize_amount <= 0:
        winnter = tkinter.Label(root, text="Draw Empty\nMerry Christmas!")
        winnter.config(font=("Ariel", 40, "bold"))
        winnter.place(relx=0.9, rely=0.05 + count, anchor="center")
    else:
        # Random Number
        qty = guest_number
        number_new = generate_random(list1)

        result = str(0) + str(number_new)
        output = result + '\n'

        # Display results to .txt
        ##Save to Winner_List.txt
        output_to_txt(output)

        # Display results on window
        shown = '#' + str(prize_amount) + ': ' + result
        winnter = tkinter.Label(root, text=shown)
        winnter.config(font=("Ariel", 50, "bold"))
        winnter.place(relx=0.9, rely=0.05 + count, anchor="center")
        count = count + 0.09

def press(event):
    button_1.configure(bg='green')


def release(event):
    button_1.configure(bg='grey')
    refresh(event)


#Setup Home_page Window
root = Tk()
root.title('Christmas Dinner ')

#Background image
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
root.overrideredirect(True)
root.configure(background='white')
image = Image.open('tree_hq.jpg')
new_image = image.resize((int(w*4/5), h))
bg = ImageTk.PhotoImage(new_image)

#Background location
root.geometry('%dx%d' % (w,h))
label = Label(root,image=bg)
label.place(x=0,y=0)

#winner_list location
Header = tkinter.Label(root, text="Winner: ")
Header.config(font=("Ariel", 70,"bold"))
#root.overrideredirect(True)
Header.place(relx=0.9, rely=0.05, anchor="center")

# GIFs
gitImage ='corpped_gif.gif'
openImage =Image.open(gitImage)

image_777=Image.open('idle.jpg')
new_image = image_777.resize((410, 310))
bg_idle = ImageTk.PhotoImage(new_image)

# Entry for guest_number
guest_number_label=tkinter.Label(root, text="# of Guests: ",font=("Ariel", int(30*w/1536),"bold"), bg="red")
guest_number_label.place(relx=0.1, rely=0.35, anchor="s")
guest_number_entry=tkinter.Entry(root,font=("Ariel", int(30*w/1536),"bold"), width=5)
guest_number_entry.place(relx=0.1, rely=0.35, anchor="n")

# Buttom
button_1 = Button(root, text="START",font=("Courier", 50),bg= 'grey',activebackground='green')
button_1.bind("<Button-1>", refresh)

root.bind("<KeyPress>", press)
root.bind("<KeyRelease>", release)

button_1.place(relx=0.4, rely=0.75, anchor="center")



## adding bg music
#url="Jingle-Bells-3.mp3"
#pygame.mixer.init()
#m=pygame.mixer.music.load(url)
#pygame.mixer.music.play()



root.mainloop()
