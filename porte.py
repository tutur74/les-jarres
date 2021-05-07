# coding: utf-8

from Tkinter import *

window = Tk()

# creer la fenetre
window.geometry('1580x850+200+90')
window.minsize(1580, 850)
window.maxsize(1580, 850)
window.title('les jarres')
window.config(background='#a41f1f')

# ajouter les écritures
bienvenue = Label(window, text='choisissez votre niveau', background='#a41f1f', font=('courrier', 30))
bienvenue.pack()

# ajout d'une frame
group_image = Frame(window, bg='#a41f1f', bd=1 , relief=SUNKEN)

# ajouter des images
image_jarre_1 = PhotoImage(file="image/porte.gif").subsample(1)
canvas = Canvas(group_image, width=220, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=image_jarre_1)
canvas.pack(side='left', padx='40')

image_jarre_2 = PhotoImage(file="image/porte.gif").subsample(1)
canvas = Canvas(group_image, width=220, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=image_jarre_2)
canvas.pack(side='left', padx='40')

image_jarre_3 = PhotoImage(file="image/porte.gif").subsample(1)
canvas = Canvas(group_image, width=210, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=image_jarre_3)
canvas.pack(side='left', padx='40')

image_jarre_4 = PhotoImage(file="image/porte.gif").subsample(1)
canvas = Canvas(group_image, width=210, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=image_jarre_4)
canvas.pack(side='left', padx='40')

image_jarre_5 = PhotoImage(file="image/porte.gif").subsample(1)
canvas = Canvas(group_image, width=220, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=image_jarre_5)
canvas.pack(side='left', padx='40')

group_image.pack(pady='110', padx='80')

# creer une frame pour les bouttons
group_bouton = Frame(window, bg='#a41f1f')

jarre_1 = Button(window, text="porte 1", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_1.pack(side='left', padx='150')

jarre_2 = Button(window, text="porte 2", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_2.pack(side='left', padx='70')

jarre_3 = Button(window, text="porte 3", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_3.pack(side='left', padx='140')

jarre_4 = Button(window, text="porte 4", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_4.pack(side='left', padx='100')

jarre_5 = Button(window, text="porte 5", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_5.pack(side='left', padx='100')


group_bouton.pack(side='left')


window.mainloop()