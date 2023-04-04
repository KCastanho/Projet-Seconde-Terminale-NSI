from random import randint, choice
from time import sleep
from davistk import *
import copy

def initialise_jeu(taille):
    assert taille % 2 == 0
    jeu = {
        "plateau": [],
        "joueur actif": "joueur1",
        "joueur1":  {
                "nom": "joueur1",
                "couleur": "white",
                "score": 2 
            },
        "joueur2":  {
                "nom": "joueur2",
                "couleur": "red",
                "score": 2 
            },
        "parametres":{
            'framerate': 10,
            'plateau' : taille,
            'taille_fenetre' : 640
            },
        "fin": False
        }
    for i in range(taille):
        jeu['plateau'].append([None] * taille)
    jeu['plateau'][taille // 2 - 1][taille // 2 - 1] = "joueur1"
    jeu['plateau'][taille // 2 ][taille // 2 ] = "joueur1"
    jeu['plateau'][taille // 2 ][taille // 2 - 1] = "joueur2"
    jeu['plateau'][taille // 2 - 1][taille // 2 ] = "joueur2"
    return jeu

def affiche(plateau):
    lst = []
    for ligne in plateau:
        lstligne = []
        for cell in ligne:
            if cell == None:
                lstligne.append(" ")
            elif cell =="joueur1":
                lstligne.append("1")
            else:
                lstligne.append("2")
        lst.append("| " + " | ".join(lstligne) + " |")
    return "\n".join(lst)

def autre_joueur(joueur):
    if joueur == "joueur1":
        return "joueur2"
    elif joueur == "joueur2":
        return "joueur1"

def case_appartient_plateau(jeu, case):
    plateau = jeu['plateau']
    i, j = case
    if -1 < i < len(plateau) and -1 < j < len(plateau):
        return True
    else:
        return False

def coup_possible_direction(jeu, coup, dir):
    plateau = jeu['plateau']
    joueur_actif = jeu['joueur actif']
    autrejoueur = autre_joueur(joueur_actif)
    i, j = coup
    dx, dy = dir
    x, y = i + dx, j + dy
    lstdir = []
    if plateau[i][j] is not None:
        return []
    while case_appartient_plateau(jeu, (x, y)) and plateau[x][y] == autrejoueur:
        lstdir.append((x, y))
        x, y = x + dx, y + dy
    if case_appartient_plateau(jeu, (x, y)) and plateau[x][y] == joueur_actif:
        return lstdir
    else:
        return []

def coup_possible(jeu, coup):
    lst = []
    directions = [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
    for dir in directions:
        lst.extend(coup_possible_direction(jeu, coup, dir))
    return lst

def coups_possibles(jeu):
    plateau = jeu['plateau']
    dico = {}
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            possible = coup_possible(jeu, (i, j))
            if len(possible) != 0:
                dico[(i,j)] = possible
    return dico

def jouer_coup(jeu, coup, dico_coups_possibles):
    plateau = jeu['plateau']
    joueur_actif = jeu['joueur actif']
    autrejoueur = autre_joueur(joueur_actif)
    score_coup = 0
    i, j = coup
    plateau[i][j] = joueur_actif
    for case in dico_coups_possibles[coup]:
        i, j = case
        plateau[i][j] = joueur_actif
        score_coup += 1
    jeu[joueur_actif]['score'] += score_coup + 1
    jeu[autrejoueur]['score'] -= score_coup
    jeu['joueur actif'] = autrejoueur



def case_vers_pixel(case, parametres):
    """
	Fonction recevant les coordonnées d'une case du plateau sous la
	forme d'un couple d'entiers (ligne, colonne) et renvoyant les
	coordonnées du pixel se trouvant au centre de cette case. Ce calcul
	prend en compte la taille de chaque case, donnée par la variable
	globale taille_case.
    """
    i, j = case
    taille_case = parametres['taille_fenetre'] // parametres['plateau']
    return (i + .5) * taille_case, (j + .5) * taille_case

def pixel_vers_case(pixel, parametres):
    """
	Fonction recevant les coordonnées d'une case du plateau sous la
	forme d'un couple d'entiers (ligne, colonne) et renvoyant les
	coordonnées du pixel se trouvant au centre de cette case. Ce calcul
	prend en compte la taille de chaque case, donnée par la variable
	globale taille_case.
    """
    i, j = pixel
    taille_case = parametres['taille_fenetre'] // parametres['plateau']
    return i // taille_case, j // taille_case


def affichage_plateau(jeu):
    taille_case = jeu['parametres']['taille_fenetre'] // jeu['parametres']['plateau']
    rectangle(0,0,10,10,remplissage=jeu[jeu['joueur actif']]['couleur'])
    for i in range(jeu['parametres']['plateau']):
        ligne(i * taille_case, 0, i * taille_case, jeu['parametres']['taille_fenetre'])
        ligne(0, i * taille_case, jeu['parametres']['taille_fenetre'], i * taille_case)
    for i in range(len(jeu['plateau'])):
        for j in range(len(jeu['plateau'])):
            if jeu['plateau'][i][j] != None:
                x, y = case_vers_pixel((i, j), jeu['parametres'])
                cercle(x, y, taille_case // 2, remplissage=jeu[jeu['plateau'][i][j]]['couleur'])


def fin_de_jeu(jeu):
    if jeu['joueur1']['score'] + jeu['joueur2']['score'] == jeu['parametres']['plateau'] ** 2:
        return True
    if len(coups_possibles(jeu)) == 0:
        return True
    return False

if __name__ == "__main__":

    jeu = initialise_jeu(6)
    cree_fenetre(jeu['parametres']['taille_fenetre'], jeu['parametres']['taille_fenetre'])

    while not jeu['fin']:
        efface_tout()
        affichage_plateau(jeu)
        mise_a_jour()

        ev = donne_ev()
        ty = type_ev(ev)
        if ty == 'Quitte':
            jeu['fin'] = True
        elif ty == 'ClicGauche':
            coup = pixel_vers_case((abscisse(ev), ordonnee(ev)),jeu['parametres'])
            dico_coups_possibles = coups_possibles(jeu)
            if coup in dico_coups_possibles:
                jouer_coup(jeu, coup, dico_coups_possibles)
                jeu['fin'] = fin_de_jeu(jeu)
        sleep(1/jeu['parametres']['framerate'])
    efface_tout()
    affichage_plateau(jeu)
    mise_a_jour()
    texte(320, 320, "Score: " + str(jeu['joueur1']['score']) + " - " + str(jeu['joueur2']['score']), couleur="red", ancrage='center')
    attend_fermeture()
