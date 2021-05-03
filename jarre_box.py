# coding: utf-8

from Tkinter import *

# creer le fenetre
window = Tk()
window.geometry('1080x730+400+150')
window.title('les jarres')
window.config(background='#a41f1f')

# ajouter les écritures
bienvenue = Label(window, text='Bienvenue dans le jeu des jarres', background='#a41f1f', font=('courrier', 30))
bienvenue.pack()

regle = Label(window, text ="il y a 5 jarres, Le but est d'ouvrir une jarre sans serpent,\n a chaque bonne jarre tu gagnes"
                          " une cle,\n au bout de trois cles tu deviens le roi du temple,\n quand tu ouvre une jarre avec "
                          "un serpent tu perds une cle,\n il y a trois niveau,le niveau 1 et le plus simple avec un serpent "
                          "dans une jarre et le niveau 3 le plus difficile avec 3 serpents", background='#a41f1f', font=('Arial', 15))
regle.pack(pady=200)

button_OK = Button(window, text="OK", background='black', font=('Arial', 15), fg='#a41f1f', relief='raised', cursor='circle')
button_OK.pack(pady=0)

window.mainloop()
