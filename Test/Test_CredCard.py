import unittest
from models.model import CredCard
from models.validation import Startwith, Exactly16, Digits,Group4, Consecutive


class TestCredCar(unittest.TestCase):
    def setUp(self):
        self.credCard = CredCard('Charles Tenorio', '622-2368-7954-3214', '12/21')

    def test_initial_number(self):
        st = Startwith()

        self.assertEquals('Valid', st.validate(self.credCard.card_number))


    def test_max_legnt(self):
        Ext = Exactly16()
        self.assertEquals('Valid', Ext.validate('4253625879615786'))

    def test_card_isnumber(self):
        dg = Digits()
        self.credCard.card_number = '4424424424442444'
        self.assertEquals('Valid', dg.validate(self.credCard.card_number))


    def test_num_of_underscore(self):
        self.credCard.card_number = '5122-2368-7954-3214'
        g4 = Group4()
        self.assertEquals('Valid', g4.validate(self.credCard.card_number))


    def test_count_character_sequence(self):
        self.credCard.card_number = '442444424442444'
        cs= Consecutive()
        self.assertEquals('Valid', cs.validate(self.credCard.card_number))




