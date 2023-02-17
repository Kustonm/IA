from __future__ import print_function, division

import unittest
from Cartas import Carta, Mazo


class Test(unittest.TestCase):

    def testMazoEliminar(self):
        mazo = Mazo()
        mazo.imprimir()
        carta23 = Carta(2, 3)
        print("se va a eliminar la carta: {0}".format(carta23))
        mazo.eliminar_carta(carta23)
        mazo.imprimir()
        self.assertFalse(mazo.esta_carta(carta23))

if __name__ == "__main__":
    unittest.main()
