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


class TestGroup(unittest.TestCase):

    def setUp(self):
        self.bob = Student('Bob', 1.72, 60, 0.13, 'Computer')
        self.charlie = Student('Charlie', 1.80, 70, 0.15, 'Civil')
        self.alice = Person('Alice', 1.65, 45, 0.12)

        # 社團
        self.fit = HighShoolClub('Fit ABC')

    def test_group_bmi(self):
        ' 加入一群人後，群體 bmi 要正確 '
        self.fit.add(self.bob)
        self.fit.add(self.charlie)
        self.fit.add(self.alice)

        self.assertAlmostEqual(self.fit.avgBMI(), 19.45, 1)

    def test_query_by_inbody(self):
        ' 找出一個群組中，健康的人、過重的、過輕的 '
        self.fit.add(self.bob)
        self.fit.add(self.charlie)
        self.fit.add(self.alice)

        self.assertEqual(self.fit.queryByInbody(
            Inbody.FIT), {self.bob, self.charlie})
        self.assertEqual(self.fit.queryByInbody(
            Inbody.TOO_LIGHT), {self.alice})
        self.assertEqual(self.fit.queryByInbody(Inbody.OVER_WEIGHTED), None)

    def test_add(self):
        self.fit.add(self.bob)
        # print("***", self.fit.getMembers())
        self.assertTrue(self.fit._members == [self.bob])
        # self.assertEqual(self.bob._groups, [self.fit])

if __name__ == '__main__':
    unittest.main()
