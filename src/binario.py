import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from modulo1.funciones import esBinario
from modulo2.clases import UI

def main():
    ui = UI()
    ui.cabecera("Binario")
    while True:
        dato = input("Introduce un número binario o escribe la palabra 'salir' para finalizar: ")
        if dato.lower() == 'salir': break
        
        if esBinario(dato):
            print(f"Número decimal: {int(dato, 2)}")
        else:
            print("No es un número binario.")

if __name__ == "__main__":
    main()