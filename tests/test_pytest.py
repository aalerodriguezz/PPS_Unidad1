import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.modulo1.funciones import esBinario

def test_es_binario_simple():
    assert esBinario("11101") == True
    assert esBinario("alechico") == False