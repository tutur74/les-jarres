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

regle = Label(frame,
              text="il y a 5 porte, Le but est d'ouvrir une porte sans lion,\n a chaque bonne porte tu gagnes une cle,\n au bout de trois cles tu peux ouvrir la porte et récuperer le trésor,\n quand tu ouvre une porte avec un lion tu perds une cle,\n il y a trois niveau,le niveau 1 et le plus simple avec un lion et le niveau 3 le plus difficile avec 3 lion",
               background='#a41f1f', font=('Arial', 15))
regle.pack()


frame.pack(expand=YES)





'''choisir son niveau'''





# ajouter les écritures
choisir_niveau = Label(window, text='choisissez votre niveau', background='#a41f1f', font=('courrier', 30))


# ajout d'une frame
group_image = Frame(window, bg='#a41f1f')

# ajouter des images
pouce = PhotoImage(file="image/pouce.gif").subsample(2)
canvas = Canvas(group_image, width=590, height=270, bg="#a41f1f", bd=0, highlightthickness=0)
canvas.create_image(00, 00, anchor=NW, image=pouce)


diable = PhotoImage(file="image/diable.gif").subsample(1)
canvas_2 = Canvas(group_image, width=220, height=210, bg="#a41f1f", bd=0, highlightthickness=0)
canvas_2.create_image(00, 00, anchor=NW, image=diable)


sueur = PhotoImage(file="image/sueur.gif").subsample(1)
canvas_3 = Canvas(group_image, width=620, height=210, bg="#a41f1f", bd=0, highlightthickness=0)
canvas_3.create_image(00, 00, anchor=NW, image=sueur)






'''choisir sa porte'''






# ajouter les écritures
bienvenue_2 = Label(window, text='choisissez votre niveau', background='#a41f1f', font=('courrier', 30))


# ajout d'une frame
group_image_2 = Frame(window, bg='#a41f1f')


# ajouter des images
image_jarre_1 = PhotoImage(file="image/porte.gif").subsample(1)
canvas_2_1 = Canvas(group_image, width=220, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas_2_1.create_image(00, 00, anchor=NW, image=image_jarre_1)


image_jarre_2 = PhotoImage(file="image/porte.gif").subsample(1)
canvas_2_2 = Canvas(group_image, width=220, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas_2_2.create_image(00, 00, anchor=NW, image=image_jarre_2)


image_jarre_3 = PhotoImage(file="image/porte.gif").subsample(1)
canvas_2_3 = Canvas(group_image, width=210, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas_2_3.create_image(00, 00, anchor=NW, image=image_jarre_3)


image_jarre_4 = PhotoImage(file="image/porte.gif").subsample(1)
canvas_2_4 = Canvas(group_image, width=210, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas_2_4.create_image(00, 00, anchor=NW, image=image_jarre_4)


image_jarre_5 = PhotoImage(file="image/porte.gif").subsample(1)
canvas_2_5 = Canvas(group_image, width=220, height=300, bg="#a41f1f", bd=0, highlightthickness=0)
canvas_2_5.create_image(00, 00, anchor=NW, image=image_jarre_5)




# creer une frame pour les bouttons
group_bouton_2 = Frame(window, bg='#a41f1f')

jarre_1 = Button(window, text="porte 1", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                 cursor='circle')


jarre_2 = Button(window, text="porte 2", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                 cursor='circle')


jarre_3 = Button(window, text="porte 3", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                 cursor='circle')


jarre_4 = Button(window, text="porte 4", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                 cursor='circle')


jarre_5 = Button(window, text="porte 5", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                 cursor='circle')




def passage_a_porte():
    choisir_niveau.destroy()
    canvas.destroy()
    canvas_2.destroy()
    canvas_3.destroy()
    group_image.destroy()
    niveau_1.destroy()
    niveau_2.destroy()
    niveau_3.destroy()
    group_bouton.destroy()
    bienvenue_2.pack()
    canvas_2_1.pack(side='left', padx='40')
    canvas_2_2.pack(side='left', padx='40')
    canvas_2_3.pack(side='left', padx='40')
    canvas_2_4.pack(side='left', padx='40')
    canvas_2_5.pack(side='left', padx='40')
    group_image_2.pack(pady='110', padx='80')
    jarre_1.pack(side='left', padx='150')
    jarre_2.pack(side='left', padx='70')
    jarre_3.pack(side='left', padx='140')
    jarre_4.pack(side='left', padx='100')
    jarre_5.pack(side='left', padx='100')
    group_bouton_2.pack(side='left')


# creer une frame pour les bouttons
group_bouton = Frame(window, bg='#a41f1f')

niveau_1 = Button(window, text="niveau 1", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                  cursor='circle', command=partial(passage_a_porte))


niveau_2 = Button(window, text="niveau 2", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                  cursor='circle', command=partial(passage_a_porte))


niveau_3 = Button(window, text="niveau 3", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                  cursor='circle', command=partial(passage_a_porte))




def passage_a_Niveau():
    frame.destroy()
    button_OK.destroy()
    choisir_niveau.pack()
    canvas.pack(side='left')
    canvas_2.pack(side='right')
    canvas_3.pack(expand=YES)
    group_image.pack(side='top', pady='110', padx='100')
    niveau_1.pack(side='left', padx='160')
    niveau_2.pack(side='left', padx='350')
    niveau_3.pack(side='left', padx='130')
    group_bouton.pack()

# ajout d'un bouton
button_OK = Button(window, text="OK", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised',
                   cursor='circle', command=partial(passage_a_Niveau))
button_OK.pack(expand=YES)


window.mainloop()