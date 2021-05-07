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
group_image = Frame(window, bg='#a41f1f')

# ajouter des images
image_jarre_1 = PhotoImage(file="image/pouce.gif").subsample(2)
canvas = Canvas(group_image, width=200, height=300, bg="#a41f1f", )
canvas.create_image(00, 00, anchor=NW, image=image_jarre_1)
canvas.pack(side='left')

image_jarre_2 = PhotoImage(file="image/diable.gif").subsample(1)
canvas = Canvas(group_image, width=200, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=image_jarre_2)
canvas.pack(side='right')

image_jarre_3 = PhotoImage(file="image/sueur.gif").subsample(1)
canvas = Canvas(group_image, width=200, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=image_jarre_3)
canvas.pack()

image_jarre_4 = PhotoImage(file="image/sueur.gif").subsample(1)
canvas = Canvas(group_image, width=200, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=image_jarre_4)
canvas.pack()

image_jarre_5 = PhotoImage(file="image/sueur.gif").subsample(1)
canvas = Canvas(group_image, width=200, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=image_jarre_5)
canvas.pack()

group_image.pack(side='top', pady='110', padx='100')

# creer une frame pour les bouttons
group_bouton = Frame(window, bg='#a41f1f')

jarre_1 = Button(window, text="niveau 1", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_1.pack(side='left', padx='160')

jarre_2 = Button(window, text="niveau 2", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_2.pack(side='left', padx='350')

jarre_3 = Button(window, text="niveau 3", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_3.pack(side='left', padx='130')

jarre_4 = Button(window, text="niveau 3", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_4.pack(side='left', padx='130')

jarre_5 = Button(window, text="niveau 3", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
jarre_5.pack(side='left', padx='130')

group_bouton.pack()


window.mainloop()