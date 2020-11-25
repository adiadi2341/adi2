from unittest import TestCase, mock
from unittest.mock import patch
from Project.Worker import Worker
import requests


class TestWorker(TestCase):
    def setUp(self):
        print("setUp")
        self.bob = Worker("bob", "mar", 1999, 11, 28, "afula", "israel")
        self.other = Worker("sagi", "bond", 2000, 11, 30, "rehovot", "literli rehov")

    def tearDown(self):
        print("tearDown")

    @mock.patch("Project.Worker.Worker.full_name", return_value='Gay!')
    def test_full_name(self,mock_fullname):
        self.assertEqual( self.bob.full_name() , "Gay!")

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
        self.assertTrue(self.bob.greet(self.other), 'bob says hello to sagi')

    # @mock.patch("Project.Worker.Worker.location", return_value='Gay!')
    def test_location(self):
        with patch('requests.get') as gay:
            gay.return_value.ok=True
            gay.return_value.text='success'
            self.assertEqual(self.bob.location(),'success')
            gay.return_value.ok=False
            self.assertEqual(self.bob.location(),'Bad response!')

        # print(self.bob.location())
        # self.assertEqual('Gay!', self.bob.location())