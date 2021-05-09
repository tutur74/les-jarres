
import random


print('Bienvenue dans le jeu des jarres')
print('il y a 5 jarres')
print("Le but est d'ouvrir une jarre sans serpent")
print("a chaque bonne jarre tu gagnes une cle, au bout de trois cles tu deviens le roi du temple")
print("quand tu ouvre une jarre avec un serpent, tu perds une cle")
print("il y a trois niveau, le niveau 1 et le plus simple avec un serpent dans une jarre et le niveau 3 le plus difficile avec 3 serpents")

niveau = int(input('choisi ton nivequ de difficulte: 1,2,3 : '))


def jeu():
    rejouer = str("oui")

    while rejouer == "oui":
        nbr_cle = 0
        while nbr_cle != 3:

            random1 = random.randint(1, 5)
            random2 = random.randint(1, 5)
            random3 = random.randint(1, 5)

            while random2 == random1:
                random2 = random.randint(1, 5)

            while random3 in [random1, random2]:
                random3 = random.randint(1, 5)

            serpent = int(0)

            if niveau == 1:
                serpent = [random1]
            elif niveau == 2:
                serpent = [random1, random2]
            elif niveau == 3:
                serpent = [random1, random2, random3]

            if niveau not in [1,2,3]:
                print('erreur')

            nbr_joueur = int(input('choisi une jarre(1, 2, 3, 4, 5) : '))

            if nbr_joueur in serpent:
                print('Perdu, un serpent apparait')
                if nbr_cle > 0:
                    nbr_cle -= 1
            else:
                print ('Bravo !')
                print('la jarre infecte etait la ' + str(serpent))
                nbr_cle += 1
                if nbr_cle == 3:
                    print('Bravo tu as 3 cle ')
                    print('tu devient le roi du temple')
                    rejouer = input('veux tu rejouer?')
                else:
                    print('tu as ' + str(nbr_cle) + 'cle')

jeu()