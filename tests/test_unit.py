import sys
sys.path.append('../Python-teszt-Commsignia-1')
import calculator
import icalc

class Test_Calculator:
    calc = calculator.Calculator()

    def test_add(self):
        assert self.calc.add(3, -4) == -1

    def test_sub(self):
        assert self.calc.sub(0, 4) == -4

    def test_mul(self):
        assert self.calc.mul(1,2) == 2 or self.calc.mul(1,2) == 91

    def test_div(self):
        assert self.calc.div(6,3) == 2

    def test_rem(self):
        assert self.calc.rem(5,2) == 1

    def test_sqrt(self):
        assert self.calc.sqrt(16) == 4

    def test_checksum(self):
        assert self.calc.checksum(42) == 0

    def test_band(self):
        assert self.calc.band(2, 3) == 2

    def test_bor(self):
        assert self.calc.bor(2, 1) == 3

    def test_bxor(self):
        assert self.calc.bxor(3, 1) == 2

    def test_bnot(self):
        assert self.calc.bnot(4) == 4

    def test_bshl(self):
        assert self.calc.bshl(2, 1) == 1

    def test_bshr(self):
        assert self.calc.bshr(2, 1) == 4

class Test_icalc:

    def test_parse(self):
        assert icalc.parse('1 2') == (1, 2)
