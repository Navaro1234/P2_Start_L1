def initialiseer_bord():
    # bord = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    bord = []
    for rij in range(3):
        rij_inhoud = []
        for kolom in range(3):
            rij_inhoud.append(' ')
        bord.append(rij_inhoud)
    return bord


def zet(bord, rij, kolom, speler):
    bord[rij][kolom] = speler
    return bord



def print_bord(bord):
    print("\n") # dit print een lijn.
    for rij in bord:
        print("|".join(rij))
        print("-" * 5)


def controleer_winnaar(bord):
    pass


def controleer_horizontaal(bord):
    pass


def controleer_verticaal(bord):
    pass


def controleer_diagonaal(bord):
    pass