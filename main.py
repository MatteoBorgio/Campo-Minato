import random as r

def genera_griglia(dimensione: int) -> list[list]:
    """
    Genera una griglia di gioco con mine posizionate casualmente.

    Args:
        dimensione (int): La dimensione della griglia (N x N).

    Returns:
        list: La griglia di gioco.
    """
    griglia = []
    for _ in range(dimensione):
        riga = []
        for i in range(dimensione):
            riga.append(" ")
        griglia.append(riga)
    return griglia

def posiziona_mine(griglia: list[list], numero_mine: int) -> None:
    """
    Posiziona le mine nella griglia di gioco.

    Args:
        griglia (list): La griglia di gioco.
        numero_mine (int): Il numero di mine da posizionare.
    """
    while numero_mine > 0:
        posizione_casuale = (r.randint(0, len(griglia) - 1), r.randint(0, len(griglia) - 1))
        if griglia[posizione_casuale[0]][posizione_casuale[1]] == " ":
            griglia[posizione_casuale[0]][posizione_casuale[1]] = "X"
            numero_mine -= 1

def calcola_numeri(griglia: list[list]) -> None:
    """
    Calcola il numero di mine adiacenti per ogni cella.

    Args:
        griglia (list): La griglia di gioco.
    """
    
    direzioni = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for i in range(len(griglia)):
        for j in range(len(griglia[i])):
            if griglia[i][j] != "X":
                conteggio_mine = 0
                for dx, dy in direzioni:
                    x, y = i + dx, j + dy
                    if 0 <= x < len(griglia) and 0 <= y < len(griglia[i]) and griglia[x][y] == "X":
                        conteggio_mine += 1
                griglia[i][j] = str(conteggio_mine)

def rivela_cella(griglia: list[list], riga: int, colonna: int) -> bool:
    """
    Rivela il contenuto di una cella.

    Args:
        griglia (list): La griglia di gioco.
        riga (int): La riga della cella.
        colonna (int): La colonna della cella.

    Returns:
        bool: True se la cella contiene una mina, False altrimenti.
    """
    if griglia[riga][colonna] == "X":
        return True
    else:
        return False

def visualizza_griglia(griglia: list[list], celle_rivelate: list[tuple]) -> None:
    """
    Visualizza la griglia di gioco.

    Args:
        griglia (list): La griglia di gioco.
        celle_rivelate (set): L'insieme delle celle rivelate.
    """
    for i in range(len(griglia)):
        for j in range(len(griglia[i])):
            if (i, j) in celle_rivelate:
                print(griglia[i][j], end=" ")
            else:
                print("?", end=" ")
        print()

def gioco_finito(griglia: list[list], celle_rivelate: list[tuple]) -> bool:
    """
    Verifica se il gioco è finito.

    Args:
        griglia (list): La griglia di gioco.
        celle_rivelate (list): L'insieme delle celle rivelate.

    Returns:
        bool: True se il gioco è finito, False altrimenti.
    """
    for i in range(len(griglia)):
        for j in range(len(griglia[i])):
            if griglia[i][j] != "X" and (i, j) not in celle_rivelate:
                return False
    return True
def main() -> None:
    """
    Funzione principale del programma.
    """
    print("\nBenvenuto in Campo Minato!\n")
    while True:
        try:
            dimensione = int(input("Inserisci la dimensione della griglia (N) (minimo 3): "))
            print()
            if dimensione <= 2:
                raise ValueError
            break
        except ValueError:
            print("Inserisci una dimensione valida. Riprova.")

    griglia = genera_griglia(dimensione)
    celle_rivelate = []
    numero_mine = int(dimensione * dimensione * 0.25)
    posiziona_mine(griglia, numero_mine)
    calcola_numeri(griglia)
    print(f"Le mine presenti sono: {numero_mine}. Buona fortuna!\n")

    while gioco_finito(griglia, celle_rivelate) == False:

        visualizza_griglia(griglia, celle_rivelate)

        while True:
            try:
                riga = int(input(f"\nInserisci la riga (0-{dimensione - 1}): "))
                if riga < 0 or riga >= dimensione:
                    raise ValueError
                colonna = int(input(f"Inserisci la colonna (0-{dimensione - 1}): "))
                print()
                if colonna < 0 or colonna >= dimensione:
                    raise ValueError
                break
            except ValueError:
                print("Inserisci una riga e colonna valide.")

        if rivela_cella(griglia, riga, colonna):
            print("Hai colpito una mina! Game Over.\n")
            visualizza_griglia(griglia, set((i, j) for i in range(dimensione) for j in range(dimensione)))
            return 
        else:
            celle_rivelate.append((riga, colonna))

    visualizza_griglia(griglia, set((i, j) for i in range(dimensione) for j in range(dimensione)))
    print("\nHai rivelato tutte le celle senza colpire una mina! Hai vinto!")
    return 

if __name__ == "__main__":
    main()
