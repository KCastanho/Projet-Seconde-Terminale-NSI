from random import randint
def jeu_de_nim () :
  print ("Bienvenue sur un jeu de Nim fait part deux lycéens.")
  print()
  print ("Les règles sont simples, vous disposez de 21 allumettes mais vous ne devez pas retirer la dernière et en ayant seulement le droit de retirer minimum 1 et maximum 3 allumettes à chaque tour, puisque vous devrez affronter l'ordinateur.")
  print ("Bonne chance, JOUEUR.")
  print()
  print ("Commençons")
  allumettes = 21
  while allumettes > 0 :
    print ("Il vous reste", allumettes, "allumettes.")
    print ("Combien en prenez-vous ?")
    
    Joueur = int(input())
    while (Joueur > 3) or (Joueur == 0) :
      print ("Veuillez insérer un chiffre compris entre 1 et 3")
      Joueur = int(input())
    allumettes = allumettes - Joueur
    if allumettes == 1:
      return print ("Vous avez gagné, bien joué :)")
    if allumettes == 0:
      return print ("Vous avez perdu, domage :(")
    Ordinateur = (randint(1,3))
    print ("Je prends", Ordinateur , "allumettes")
    allumettes = allumettes - Ordinateur 
    if allumettes == 1:
      return print ("Vous avez perdu, domage :(")
    if allumettes == 0:
      return print ("Vous avez gagner, bien joué :)")  
  while allumettes == 2:
    Ordinateurn = (randint(1))
  while allumettes == 3:
    Ordinateur = (randint(2))
  while allumettes == 4:
    Ordinateur = (randint(3))

jeu_de_nim () 
print()
print ("Merci d'avoir joué et testé notre jeu.")
