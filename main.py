import tkinter
import customtkinter
import pygame

from PIL import Image, ImageTk

from threading import*
import time
import math

####################################################

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green


root = customtkinter.CTk()

root.title("Music Player")
root.geometry("400x480")
root.configure(bg='#02103c')

pygame.mixer.init()

list_of_songs = ['music/City.wav']
list_of_covers = ['images/city.jpg']
n=0

def get_album_cover(song_name,n):
    image1 = Image.open(list_of_covers[n])
    image2=image1.resize((250, 250))
    load = ImageTk.PhotoImage(image2)
    label1 = tkinter.Label(root, image=load)
    label1.image = load
    label1.place(relx=0.25, rely=0.06)


    stripped_string = song_name[6:-4]
    song_name_label=tkinter.Label(text=stripped_string, bg='#222222',fg='white')
    song_name_label.place(relx=0.4, rely=0.6)



def progress():
    a =  pygame.mixer.Sound(f'{list_of_covers[n]}')
    song_len = a.get_length() * 3
    for i in range(0, math.ceil(song_len)):
        time.sleep(0.3)
        progressbar.set(pygame.mixer.music.get_pos()/1000000)

def threading():
    t1=Thread(target=progress)
    t1.start()

def play_music():
    threading()
    global n
    current_song = n
    if n > 2:
        n=0
    song_name=list_of_songs[n]
    pygame.mixer.music.load(song_name)
    pygame.mixer.music.play(loops=0)
    pygame.mixer.music.set_volume(0.5)
    get_album_cover(song_name,n)

    n+=1

def skip_ff():
    play_music()

def skip_b():
    global n
    n-=2
    play_music()

def volume(value):
    print(value)
    pygame.mixer.music.set_volume(value)





# Button
play_button = customtkinter.CTkButton(master=root, text='Play', command=play_music)
play_button.place(relx=0.5,rely=0.7, anchor=tkinter.CENTER)

skip_f = customtkinter.CTkButton(master=root ,text='>', command=skip_ff, width=2)
skip_f.place(relx=0.75,rely=0.7, anchor=tkinter.CENTER)
skip_f.configure(fg_color='#ade6f4')

skip_b = customtkinter.CTkButton(master=root, text='<', command=skip_b, width=2)
skip_b.place(relx=0.25,rely=0.7,anchor=tkinter.CENTER)
skip_b.configure(fg_color='#ade6f4')

slider = customtkinter.CTkSlider(master=root, from_=0,to=1, command=volume)
slider.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


progressbar = customtkinter.CTkProgressBar(master=root, progress_color='#5db5f8', width=250)
progressbar.place(relx=0.5,rely=0.85,anchor=tkinter.CENTER)

root.mainloop()


