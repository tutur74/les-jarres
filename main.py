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
frame = Frame(window, bg='#a41f1f', )

# ajouter les écritures
bienvenue = Label(frame, text='Bienvenue dans le jeu des jarres', background='#a41f1f', font=('courrier', 30))
bienvenue.pack()

regle = Label(frame, text="il y a 5 porte, Le but est d'ouvrir une porte sans lion,\n a chaque bonne porte tu gagnes une cle,\n au bout de trois cles tu peux ouvrir la porte et récuperer le trésor,\n quand tu ouvre une porte avec un lion tu perds une cle,\n il y a trois niveau,le niveau 1 et le plus simple avec un lion et le niveau 3 le plus difficile avec 3 lion", background='#a41f1f', font=('Arial', 15))
regle.pack()

frame.pack()

# ajout d'un bouton
button_OK = Button(window, text="OK", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
button_OK.pack(expand=YES)

window.mainloop()
