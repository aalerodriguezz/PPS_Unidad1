import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modulo1.funciones import estaEnRango, estaEnLista
from modulo2.clases import UI

def main():
    ui = UI()
    ui.cabecera("Listas")
    L = [6, 14, 11, 3, 2, 1, 15, 19]
    print(f"Lista: {L} | Rango: 1-20")
    
    while True:
        dato = input("Indica un número o escribre la palabra 'salir' para finalizar: ")
        if dato.lower() == 'salir': break
        try:
            n = int(dato)
            if estaEnRango(n, 1, 20):
                print("Esta en el rango.", end=" ")
                if estaEnLista(n, L): print("Y esta en la lista.")
                else: print("Pero no esta en la lista.")
            else:
                print("Esta fuera de rango.")
        except:
            print("Error: Introduce un número por favor.")

if __name__ == "__main__":
    main()