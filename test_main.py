def eh_par(numero):
    return numero % 2 == 0

print(eh_par(4))

import unittest
from main import eh_par

class TestPar(unittest.TestCase):

    def test_par(self):
        self.assertTrue(eh_par(2))

    def test_impar(self):
        self.assertFalse(eh_par(3))

if __name__ == "__main__":
    unittest.main()
