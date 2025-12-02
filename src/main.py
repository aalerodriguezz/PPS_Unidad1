import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import binario, lista
from modulo2.clases import UI

if __name__ == "__main__":
    UI().cabecera("Menú Principal")
    op = input("1. Binario\n2. Listas\nEscoge (1 o 2): ")
    if op == '1': binario.main()
    elif op == '2': lista.main()