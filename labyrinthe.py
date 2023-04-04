from pile import *
import turtle
import random


LONGUEUR_TAB = 50
HAUTEUR_TAB = 50
LONGUEUR_PAS = 8
MARGE = 8

screen = turtle.Screen()
screen.setup(LONGUEUR_TAB*LONGUEUR_PAS+2*MARGE, HAUTEUR_TAB*LONGUEUR_PAS+2*MARGE)
screen.setworldcoordinates(
    llx=-MARGE,
    lly=-HAUTEUR_TAB*LONGUEUR_PAS-MARGE,
    urx=LONGUEUR_TAB*LONGUEUR_PAS+MARGE,
    ury=MARGE
)
turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("green")
turtle.width(LONGUEUR_PAS//2)


def avancer(direction):
    """
    Avance la tortue dans la direction indiquée.
    
    Paramètres :
    ------------
        direction (str) : "H" pour haut, "B" pour bas, 
                          "D" pour droite et "G" pour gauche
    """
    dir_to_angle = {
        "H" : 90,
        "B" : -90,
        "G" : 180,
        "D" : 0
    }
    turtle.setheading(dir_to_angle[direction])
    turtle.forward(LONGUEUR_PAS)


def explorer(position, tableau):
    """
    Explore les cases adjacentes à la position indiquées.
    Renvoie en sortie l'ensemble des directions que la tortue peut prendre.
    Paramètres :
    ------------
        position (tuple) : les coordonnées de la tortue dans le tableau
        tableau (list) : le tableau des cases déjà explorées.
                         Une case n'a jamais été explorée si elle contient 0
                         Une case déjà explorée contient un 1
    Sortie :
    --------
        list : la liste de toutes les directions ("H", "B", "G", "D")
    """
    i, j = position
    s = []
    if i-1 != -1 and tableau[i-1][j] == 0:
        s.append("H")
    if i+1 != HAUTEUR_TAB and tableau[i+1][j] == 0:
        s.append("B")
    if j-1 != -1 and tableau[i][j-1] == 0:
        s.append("G")
    if j+1 != LONGUEUR_TAB and tableau[i][j+1] == 0:
        s.append("D")
    return s


def nouvelle_position(position_i, direction):
    """
    Calcule la nouvelle position de la tortue dans le tableau, sachant que
    position_i est la position initiale de la tortue, et direction est une des quatre lettres
    "H", "B", "G", "D", représentant le déplacement de la tortue.
    Paramètres :
    ------------
        position_i (tuple) : la position initiale de la tortue avant le déplacement
        direction (str) : la direction du déplacement
    Sortie :
    --------
        tuple : la nouvelle position de la tortue au format (i, j)
    Exemples :
    ----------
        nouvelle_position((1, 3), "B") doit renvoyer la position (1, 4)
    """
    i, j = position_i
    if direction == "H":
        return (i-1, j)
    elif direction == "B":
        return (i+1, j)
    elif direction == "G":
        return (i, j-1)
    elif direction == "D":
        return (i, j+1)


def marquer_passage(position, tableau):
    """
    Marque le passage de la tortue en la position (i, j), en écrivant 1
    dans la case de coordonnées (i, j) du tableau.
    Paramètres :
    ------------
        position (tuple) : la position courante de la tortue
        tableau (list) : le tableau des passages de la tortue
    Sortie :
    --------
        None : la fonction modifie le tableau, mais ne renvoie aucune valeur
    """
    i, j = position
    tableau[i][j] = 1


def main():
    
    tableau = [
        [0 for i in range(LONGUEUR_TAB)] for j in range(HAUTEUR_TAB)
    ]

    position = (0, 0)   
    marquer_passage(position, tableau)
    chemin = creer_pile_vide()
    oppose = {"H" : "B", "B" : "H", "G" : "D", "D" : "G"}


    choix_direction = random.choice(explorer(position, tableau))
    empiler(chemin, choix_direction)
    avancer(choix_direction)
    position = nouvelle_position(position, choix_direction)
    marquer_passage(position, tableau)


    while not est_vide(chemin):
        choix_possibles = explorer(position, tableau)

        if choix_possibles != []:
            choix_direction = random.choice(choix_possibles)
            empiler(chemin, choix_direction)
            turtle.pencolor("green")
            avancer(choix_direction)
            position = nouvelle_position(position, choix_direction)
            marquer_passage(position, tableau)
        else :
            choix_direction = depiler(chemin)
            turtle.pencolor("white")
            avancer(oppose[choix_direction])
            position = nouvelle_position(position, oppose[choix_direction])


    turtle.exitonclick()

main()
