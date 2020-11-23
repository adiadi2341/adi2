from unittest import TestCase
from Project.Worker import Worker

class TestWorker(TestCase):
    def setUp(self):
        print("setUp")
        self.bob = Worker("bob", "mar", 1999, 11, 28, "afula", "israel")
        self.other = Worker("sagi", "bond", 2000, 11, 30, "rehovot", "literli rehov")


    def tearDown(self):
        print("tearDown")

    def test_full_name(self):
        res = self.bob.full_name()
        print(self.bob.full_name())
        self.assertTrue(res == "bob mar")

    def test_age_past(self):
        res = self.bob.age()
        print(self.bob.age())
        self.assertTrue(res == "bob is 21 years old")

    def test_age_future(self):
        self.bob1 = Worker("bob", "mar", 2030, 11, 28, "afula", "israel")
        res = self.bob1.age()
        print(self.bob1.age())
        self.assertNotIn("-", res)

    def test_age_now(self):
        self.bob1 = Worker("bob", "mar", 2020, 11, 28, "afula", "israel")
        res = self.bob1.age()
        print(self.bob1.age())
        self.assertTrue(res == "bob is 0 years old")

    def test_days_to_birthday_future(self):
        print(self.bob.days_to_birthday())
        self.assertIn("5", self.bob.days_to_birthday())

    def test_days_to_birthday_past(self):
        self.bob1 = Worker("bob", "mar", 1999, 11, 22, "afula", "israel")
        print(self.bob1.days_to_birthday())
        self.assertIn("364", self.bob.days_to_birthday())

    def test_days_to_birthday_now(self):
        self.bob1 = Worker("bob", "mar", 1999, 11, 23, "afula", "israel")
        print(self.bob1.days_to_birthday())
        self.assertIn("0", self.bob.days_to_birthday())

    def test_greet(self):
        print(self.bob.greet(self.other))
        self.assertTrue(self.bob.greet(self.other),'bob says hello to sagi')

    # def test_location(self):
    #     print(self.bob.location())
    #     self.assertTrue(self.bob.location(),"32.60306,35.30886")