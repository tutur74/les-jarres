# coding: utf-8
from Tkinter import *
from functools import partial


# creer le fenetre
window = Tk()
window.geometry('1580x850+200+90')
window.minsize(1580, 850)
window.maxsize(1580, 850)
window.title('les jarres')
window.config(background='#a41f1f')

# ajout d'une frame
frame = Frame(window, bg='#a41f1f')

# ajouter les écritures
bienvenue = Label(frame, text='Bienvenue dans le jeu des jarres', background='#a41f1f', font=('courrier', 30))
bienvenue.pack()

regle = Label(frame, text="il y a 5 porte, Le but est d'ouvrir une porte sans lion,\n a chaque bonne porte tu gagnes une cle,\n au bout de trois cles tu peux ouvrir la porte et récuperer le trésor,\n quand tu ouvre une porte avec un lion tu perds une cle,\n il y a trois niveau,le niveau 1 et le plus simple avec un lion et le niveau 3 le plus difficile avec 3 lion", background='#a41f1f', font=('Arial', 15))
regle.pack()

frame.pack(expand=YES)


'''choisir son niveau'''


def niveau():
    # ajouter les écritures
    choisir_niveau = Label(window, text='choisissez votre niveau', background='#a41f1f', font=('courrier', 30))
    choisir_niveau.pack()

    # ajout d'une frame
    group_image = Frame(window, bg='#a41f1f')

    # ajouter des images
    pouce = PhotoImage(file="image/pouce.gif").subsample(2)
    canvas = Canvas(group_image, width=590, height=270, bg="#a41f1f", bd=0, highlightthickness=0)
    canvas.create_image(00, 00, anchor=NW, image=pouce)
    canvas.pack(side='left')

    diable = PhotoImage(file="image/diable.gif").subsample(1)
    canvas = Canvas(group_image, width=220, height=210, bg="#a41f1f", bd=0, highlightthickness=0)
    canvas.create_image(00, 00, anchor=NW, image=diable)
    canvas.pack(side='right')

    sueur = PhotoImage(file="image/sueur.gif").subsample(1)
    canvas = Canvas(group_image, width=620, height=210, bg="#a41f1f", bd=0, highlightthickness=0)
    canvas.create_image(00, 00, anchor=NW, image=sueur)
    canvas.pack(expand=YES)

    group_image.pack(side='top', pady='110', padx='100')

    # creer une frame pour les bouttons
    group_bouton = Frame(window, bg='#a41f1f')

    niveau_1 = Button(window, text="niveau 1", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                      cursor='circle')
    niveau_1.pack(side='left', padx='160')

    niveau_2 = Button(window, text="niveau 2", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                      cursor='circle')
    niveau_2.pack(side='left', padx='350')

    niveau_3 = Button(window, text="niveau 3", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                      cursor='circle')
    niveau_3.pack(side='left', padx='130')

    group_bouton.pack()

def passage_a_Niveau():
    frame.destroy()
    button_OK.destroy()
    niveau()

# ajout d'un bouton
button_OK = Button(window, text="OK", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                   cursor='circle', command=partial(passage_a_Niveau))
button_OK.pack(expand=YES)


window.mainloop()