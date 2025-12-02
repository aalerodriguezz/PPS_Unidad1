import unittest, sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.modulo1.funciones import esBinario, estaEnRango, estaEnLista

class TestM1(unittest.TestCase):
    def test_binario(self):
        self.assertTrue(esBinario("101001"))
        self.assertFalse(esBinario("23201"))
    def test_rango(self):
        self.assertTrue(estaEnRango(5,1,10))
    def test_lista(self):
        self.assertTrue(estaEnLista(1, [1,2]))

if __name__ == '__main__': unittest.main()