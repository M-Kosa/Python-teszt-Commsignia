import sys
sys.path.append('../Python-teszt-Commsignia-1')
import icalc


class Test_icalc:
    icalc = icalc.InteractiveCalculator()

    def test_do_add(self, capfd):
        self.icalc.do_add('1 2')
        out, err = capfd.readouterr()
        assert out == '3' + '\n'

    def test_do_sub(self, capfd):
        self.icalc.do_sub('1 2')
        out, err = capfd.readouterr()
        assert out == '-1' + '\n'

    def test_do_mul(self, capfd):
        self.icalc.do_mul('1 2')
        out, err = capfd.readouterr()
        assert out == '2' + '\n'
    
    def test_do_div(self, capfd):
        self.icalc.do_div('6 3')
        out, err = capfd.readouterr()
        assert out == '2' + '\n'

    def test_do_rem(self, capfd):
        self.icalc.do_rem('5 2')
        out, err = capfd.readouterr()
        assert out == '1' + '\n'

    def test_do_sqrt(self, capfd):
        self.icalc.do_sqrt('16')
        out, err = capfd.readouterr()
        assert out == '4' + '\n'
    
    def test_do_bit_and(self, capfd):
        self.icalc.do_bit_and('2 3')
        out, err = capfd.readouterr()
        assert out == '2' + '\n'

    def test_do_bit_or(self, capfd):
        self.icalc.do_bit_or('2 3')
        out, err = capfd.readouterr()
        assert out == '3' + '\n'
    
    def test_do_bit_xor(self, capfd):
        self.icalc.do_bit_xor('3 1')
        out, err = capfd.readouterr()
        assert out == '2' + '\n'

    def test_do_bit_not(self, capfd):
        self.icalc.do_bit_not('4')
        out, err = capfd.readouterr()
        assert out == '3' + '\n'

    def test_do_bit_shift_left(self, capfd):   
        self.icalc.do_bit_shift_left('2 1')
        out, err = capfd.readouterr()
        assert out == '4' + '\n'
    
    def test_do_bit_shift_right(self, capfd):
        self.icalc.do_bit_shift_right('2 1')
        out, err = capfd.readouterr()
        assert out == '1' + '\n'
    
