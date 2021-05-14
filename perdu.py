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
frame_3 = Frame(window, bg='#a41f1f')

# ajouter les écritures
bienvenue_2 = Label(frame_3, text='!!!', background='#a41f1f', font=('courrier', 30))
bienvenue_2.pack()

perdu = Label(frame_3, text ="dommage tu as perdu" ,background='#a41f1f', font=('Arial', 15))
perdu.pack()

# ajout d'un bouton
tete_de_mort = PhotoImage(file="image/sticker-tete-de-mort.gif").subsample(1)
canvas_4 = Canvas(frame_3, width=500, height=510, bg="#a41f1f", bd=0, highlightthickness=0)
canvas_4.create_image(00, 00, anchor=NW, image=tete_de_mort)
canvas_4.pack(side='top', padx=0)

frame_3.pack(expand=YES)

# ajout d'un bouton
button_OK = Button(frame_3, text="Rejouer", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
button_OK.pack(expand=YES)



window.mainloop()
