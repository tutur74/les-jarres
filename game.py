# coding: utf-8

from Tkinter import *

window = Tk()

# creer la fenetre
window.geometry('1580x850+200+90')
window.minsize(1580, 850)
window.maxsize(1580, 850)
window.title('les jarres')
window.config(background='#a41f1f')

# ajout d'une frame
group_image = Frame(window, bg='#a41f1f', )

# ajouter les écritures
bienvenue = Label(window, text='choisissez votre niveau', background='#a41f1f', font=('courrier', 30))
bienvenue.pack()

# ajouter des images
pouce = PhotoImage(file="image/pouce.gif").subsample(2)
canvas = Canvas(group_image, width=450, height=400, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=pouce)
canvas.pack(side='left')

diable = PhotoImage(file="image/diable.gif").subsample(1)
canvas = Canvas(group_image, width=420, height=210, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=diable)
canvas.pack(side='right')

sueur = PhotoImage(file="image/sueur.gif").subsample(1)
canvas = Canvas(group_image, width=420, height=210, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=sueur)
canvas.pack(expand=YES)

group_image.pack()


window.mainloop()