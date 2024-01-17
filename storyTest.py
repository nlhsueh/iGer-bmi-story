import unittest
from bmiStory import *
from healthUtil import *


class TestPerson(unittest.TestCase):

    def test_inbody(self):
        bob = Student('Bob', 1.72, 60, 0.13, 'Computer')
        charlie = Student('Charlie', 1.80, 70, 0.15, 'Civil')
        alice = Person('Alice', 1.65, 45, 0.12)

        people = [bob, charlie, alice]
        for p in people:
            self.assertTrue(p.weight < 200 and p.weight > 30)
            self.assertTrue(p.height < 2.2)
            self.assertTrue(p.bodyFat < 1)
            self.assertTrue(p.BMI < 50 and p.BMI > 10)

        self.assertEqual(charlie.name, 'Charlie')
        self.assertAlmostEqual(bob.BMI, 20.25, places=1)
        self.assertEqual(alice.inbody, Inbody.TOO_LIGHT)

        # bob 體重增到了 120
        bob.updateInbody(weight=120)
        self.assertAlmostEqual(bob.BMI, 40.56, places=1)

if __name__ == '__main__':
    unittest.main()
