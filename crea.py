#Information de base:
name = input('Nom du personnage: ')
new_carac = input('Est-ce un nouveau personnage ? (y/n) ')
if new_carac == 'y':
  niveau = 1
elif new_carac == 'n':
  continue
else:
  print('Veuillez répondre par y ou n')
  
#Determination de la Classe
classe = input('Quel classe souhaitez vous jouer ? ')
if new_carac == 'n':
  niveau = int(input('De quel niveau est le personnage ? '))
  if niveau <= 0:
    print('le niveau ne peut pas etre négatif')
  elif niveau > 3:
    sous_classe = input('Quel sous-classe avez vous choisi')
  exp = int(input("Combien de point d'expérience votre personnage a t'il gagné ? "))

# Historique
historique = input("Choisisez l'historique de votre personnage")
espèce = input()







