
from mytictactoe import *

def tic_tac_toe():
    bord = initialiseer_bord()
    huidige_speler = 'X'
    einde_spel = False
    winnaar = ''
    teller = 0

    while not einde_spel:
        print_bord(bord)
        rij = int(input("kies een rij (0, 1, 2): "))
        kolom = int(input("kies een kolom (0, 1, 2): "))

        bord = zet(bord, rij, kolom, huidige_speler)

        if huidige_speler == 'X':
            huidige_speler = 'O'
        else:
            huidige_speler = 'X'

tic_tac_toe()

