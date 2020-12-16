from django.test import TestCase,Client
# import django.test
# from util import ChatCache
# Create your tests here.

class TestViews(TestCase):
    @classmethod
    def setUpClass(cls):
        print("Start test Views")

    def test_login(self):
        response = self.client.get("/login")
        self.assertEqual(response.status_code, 301)

    def test_register(self):
        response = self.client.get("/register")
        self.assertIn(response.status_code, [200,301])
    def test_robots(self):
        response = self.client.get("http://127.0.0.1:8088/robots.txt")
        self.assertIn(response.status_code, [200,301])

    @classmethod
    def tearDownClass(cls):
        print("End test of Views")



if __name__ == "__main__":
    pass
    
