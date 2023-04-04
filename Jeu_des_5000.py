from random import randint


def lance_de():
    """ Ne pas modifier. Fonction retournant la face d'un dé équilibré.
    """
    de = randint(1, 6)
    print(de, end=" ")
    return de


def score_des(cmpt1, cmpt5):
    """ Fonction retournant le score lié au nombre de 1 et au nombre de 5. cmpt1
    correspondant au nombre de 1 et cmpt5 au nombre de 5.
    Parameters:
        cmpt1 (int): nombre de 1
        cmpt5 (int): nombre de 5
    Returns:
        (int): score correspondant
    """
    score = cmpt1 * 100 + cmpt5*50
    return score 


def lance_des(nbde):
    """ Fonction simulant le lancer de nbde dés et retournant le nombre de 1 et
    le nombre de 5. Utilise la fonction lance_de().
    Parameters:
        nbde (int): nombre de dés lancés
    Returns:
        (int, int): couple de nombre de 1 et nombre de 5 réalisés.
    """
    list_face = []
    for i in range (nbde):
        list_face.append(lance_de())
        
    cmpt1, cmpt5 = list_face.count(1), list_face.count(5)
    c1_total = cmpt1; c5_total = cmpt5

    while cmpt1+cmpt5 ==nbde :
        list_face = []
        for i in range (nbde):
            list_face.append(lance_de())
        cmpt1, cmpt5 = list_face.count(1), list_face.count(5)
        c1_total += cmpt1 ; c5_total += cmpt5

    return c1_total, c5_total


def affichage_choix_continuer(score_tour, nbde):
    """ Fonction affichant le score du tour score_tour ainsi que le nombre
    de dés encore jouable et retournant le choix du joueur concernant sa
    volonté de continuer à lancer les dés.
    Parameters:
        score_tour (int): score du tour
        nbde (int): nombre de dés encore jouable
    Returns:
        (bool): False si le joueur décide d'arrêter, True sinon
    """
    if nbde != 0:
        print('Score du tour', score_tour,'pts - Relancer',nbde,'dés')
    
    choix_joueur = input('(o/n) ?')

    if choix_joueur == 'o':
        choix = True
    else : 
        choix = False
        print('Votre score est {} . '.format(score_tour))
        if type_partie == '1':
            print('TOUR',cmpt_tour,': FIN DU TOUR.')

    return choix


def affichage_tout_perdu():
    """ Affiche que le score du tour est nul car il n'y a aucun 1 et 5.
    """

    print ('Aucun 1 ou 5. Score de ce tour : 0')


def affichage_lancer(nbde):
    """ Ne pas modifier. Affiche le nombre de dés lancer.
    """
    print("Lancer de", nbde, "dés")


def tour():
    """ Ne pas modifier. Fonction principale d'un tour. Tant que la variable
    continuer est vraie, on lance les dés, on compte les 1 et les 5.
    Si il y en a, alors on demande si on veut continuer, on ajoute le score et
    on enlève les dés 1 et 5.
    Sinon, on sort (en mettant continuer à Faux et le score du tour à 0)
    """
    continuer = True  
    nbde = 5  
    score_tour = 0  
    while continuer:
        affichage_lancer(nbde)
        cmpt1, cmpt5 = lance_des(nbde)
        score_lancer = score_des(cmpt1, cmpt5)
        if score_lancer != 0:
            score_tour += score_lancer
            nbde -= cmpt1 + cmpt5
            continuer = affichage_choix_continuer(score_tour, nbde)
        else:
            affichage_tout_perdu()
            continuer = False
            score_tour = 0
    return score_tour


""" Boucle principale du jeu. Tant que l'on est pas arrivé à 1000, on continue
 de jouer en incrémentant le numéro du tour et en ajoutant le score """

cmpt_tour = 0
type_partie= input('Entrez 1 pour un partie seule ou 2 pour une partie à deux : ')

if type_partie == '1':
    score = 0
    cmpt_tour = 0
    score_gagnant= int(input('Quel est le score à atteindre pour gagner le jeu ?'))

    while score < score_gagnant:
        cmpt_tour += 1
        print("TOUR", cmpt_tour, ": DEBUT DU TOUR. Votre score est", score)
        score += tour()

    if score >= score_gagnant:
        print ('Vous avez gagné avec', score, 'pts !')
        
else: 
    joueur1 = input('Nom joueur 1 : ') 
    joueur2 = input('Nom joueur 2 : ')
    score_joueur1= 0
    score_joueur2= 0
    score_gagnant= int(input('Quel est le score à atteindre pour gagner le jeu ?'))

    while score_joueur1 or score_joueur2 < score_gagnant :
        cmpt_tour += 1
        print("TOUR", cmpt_tour, ": DEBUT DU TOUR. Score :", joueur1,':',score_joueur1, joueur2,':', score_joueur2, 'À ton tour,', joueur1)
        score_joueur1 += tour()
        print('À ton tour,', joueur2)
        score_joueur2 += tour()
        print('TOUR',cmpt_tour,': FIN DU TOUR.')

    if score_joueur1 >= score_gagnant:
        print (joueur1,'a gagné avec', score_joueur1, 'pts !')

    elif score_joueur2 >= score_gagnant:
        print (joueur2,'a gagné avec', score_joueur2, 'pts !')
