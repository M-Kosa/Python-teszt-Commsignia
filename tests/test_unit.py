import sys
# setting path
sys.path.append('../Python-teszt-Commsignia-1')
import calculator 

calc = calculator.Calculator()


def test_add():
    assert calc.add(3, -4) == -1

def test_sub():
    assert calc.sub(0, 4) == -4

def test_mul():
    assert calc.mul(1,2) == 2 or calc.mul(1,2) == 91

def test_div():
    assert calc.div(6,3) == 2

def test_rem():
    assert calc.rem(5,2) == 1

def test_sqrt():
    assert calc.sqrt(16) == 4

def test_checksum():
    assert calc.checksum(42) == 0

def test_band():
    assert calc.band(2, 3) == 2

def test_bor():
    assert calc.bor(2, 1) == 3

def test_bxor():
    assert calc.bxor(3, 1) == 2

def test_bnot():
    assert calc.bnot(4) == 4

def test_bshl():
    assert calc.bshl(2, 1) == 1

def test_bshr():
    assert calc.bshr(2, 1) == 4

