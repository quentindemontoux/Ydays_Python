from random import randint, shuffle
import time
from Joueurs import Joueur_1 , Joueur_2

j1 = Joueur_1()

j2 = Joueur_2()

board = []

for i in range(15):
    board.append(randint(-400,-10))
for i in range(15):
    board.append(randint(10,100))

shuffle(board)

def game(x):

    des = 0
    des = (randint(1,6) + randint(1,6))
    x.position = x.position + des

    if x.position >= 30:
                
        x.position = x.position - 31
                
    else:

        x.argent = x.argent + board[(x.position)]

    print("Le joueur",x.nom ,"à fait", des)
    time.sleep(1)
    print("le joueur",x.nom ,"est sur la case", x.position, "qui est à :",board[(x.position)],"€")
    print("Le joueur",x.nom ,"à:", x.argent,"€")
    time.sleep(2)
    print("")

if __name__ == "__main__":

    print(board)
    while j1.argent > 0 and j2.argent > 0:

        game(j1)

        game(j2)

    if j1.argent <= 0:

        print("Le joueur 2 à gagné!!")

    else:

        print("Le joueur 1 à gagné!!")