# 🧨 Campo Minato in Python

Questo progetto è una semplice implementazione del gioco "Campo Minato" (Minesweeper) in Python, giocabile da terminale. 

## 🎯 Obiettivo del Gioco

L'obiettivo è rivelare tutte le celle che **non** contengono mine. Se si rivela una mina, il gioco è perso. Se si rivelano tutte le celle sicure, il gioco è vinto.

## 🛠 Funzionalità del Programma

- Generazione di una griglia quadrata N x N, con dimensioni definite dall'utente.
- Posizionamento casuale di M mine sulla griglia.
- Calcolo del numero di mine adiacenti per ogni cella.
- Interazione con l'utente per selezionare celle.
- Rivelazione delle celle con visualizzazione del numero di mine vicine o della mina 💣.
- Controllo della fine del gioco (vittoria o sconfitta).
- Visualizzazione della griglia di gioco aggiornata ad ogni turno.

## 🧠 Struttura Dati

- Ogni **cella** della griglia è rappresentata da un valore che può essere:
  - `💣` per indicare una mina.
  - Un numero intero da 0 a 8 che rappresenta il numero di mine adiacenti.
- Lo **stato** di ogni cella (rivelata o nascosta) è gestito separatamente tramite un set di celle rivelate.

## 🧩 Struttura del Codice

```python
import random

def genera_griglia(dimensione, numero_mine):
    """
    Genera una griglia di gioco con mine posizionate casualmente.
    """
    pass

def posiziona_mine(griglia, numero_mine):
    """
    Posiziona le mine nella griglia di gioco.
    """
    pass

def calcola_numeri(griglia):
    """
    Calcola il numero di mine adiacenti per ogni cella.
    """
    pass

def rivela_cella(griglia, riga, colonna):
    """
    Rivela il contenuto di una cella.
    """
    pass

def visualizza_griglia(griglia, celle_rivelate):
    """
    Visualizza la griglia di gioco.
    """
    pass

def gioco_finito(griglia, celle_rivelate):
    """
    Verifica se il gioco è finito.
    """
    pass

def main():
    """
    Funzione principale del programma.
    """
    pass

if __name__ == "__main__":
    main()

