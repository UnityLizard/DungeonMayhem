import unittest
from ability import *

class AbilityGettersTests(unittest.TestCase):
    def setUp(self):
        self.ability = Ability('Ability', 10, AbilityType.OFFENCE, 10, 10, None, 10, 10)

    def test_get_name(self):
        self.assertEqual(self.ability.get_name(), 'Ability',
                         'incorrect ability name')

    def test_get_type(self):
        self.assertEqual(self.ability.get_type(), AbilityType.OFFENCE,
                         'wrong ability type')

class AbilityCDTests(unittest.TestCase):
    def setUp(self):
        self.ability = Ability('Ability', 10, AbilityType.OFFENCE, 10, 10, None, 10, 10)

    def test_not_on_cd(self):
        self.assertEqual(self.ability.is_on_cd(), False,
                         'ability should not be on cooldown')

    def test_on_cd(self):
        self.ability.set_on_cd()
        self.assertEqual(self.ability.is_on_cd(), True,
                         'ability should be on cooldown')

    def test_reduce_cd(self):
        self.ability.set_on_cd()
        while self.ability.is_on_cd():
            self.ability.reduce_cd()
        self.assertEqual(self.ability.is_on_cd(), False,
                         'ability cooldown should have been removed')

def GetterSuite():
    suite = unittest.TestSuite()
    suite.addTest(AbilityGettersTests('test_get_name'))
    suite.addTest(AbilityGettersTests('test_get_type'))
    return suite

def CooldownSuite():
    suite = unittest.TestSuite()
    suite.addTest(AbilityCDTests('test_not_on_cd'))
    suite.addTest(AbilityCDTests('test_on_cd'))
    suite.addTest(AbilityCDTests('test_reduce_cd'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(GetterSuite())
    runner.run(CooldownSuite())