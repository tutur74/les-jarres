# coding: utf-8

from Tkinter import *

# creer le fenetre
window = Tk()
window.geometry('1580x850+200+90')
window.minsize(1580, 850)
window.maxsize(1580, 850)
window.title('les jarres')
# window.config(background='#a41f1f')
window.config(background='#a41f1f')

# ajout d'une frame
frame = Frame(window, bg='#a41f1f')

# ajouter les écritures
bienvenue = Label(frame, text='Bravo !!!', background='#a41f1f', font=('courrier', 30))
bienvenue.pack()

regle = Label(frame, text ="tu a troi clé tu arrives a ouvrir la porte et récuperer le tresor" ,background='#a41f1f', font=('Arial', 15))
regle.pack()

# ajout d'un bouton
tresor = PhotoImage(file="image/tresor.gif").subsample(1)
canvas = Canvas(frame, width=550, height=510, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=tresor)
canvas.pack(side='right')

frame.pack(expand=YES)

# ajout d'un bouton
button_OK = Button(window, text="Rejouer", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
button_OK.pack(expand=YES)

window.mainloop()
