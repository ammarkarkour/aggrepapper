import unittest
from aggrepapper import app
from fastapi.testclient import TestClient

client = TestClient(app)

class TestAggrepapper(unittest.TestCase):

    def test_list(self):
        response = client.get("/news/")
        self.assertEqual(response.status_code, 200)

        # Test that all object contain the required fields
        for news in response.json():
            self.assertTrue("headline" in news)
            self.assertTrue("link" in news)
            self.assertTrue("source" in news)

    def test_search(self):
        response = client.get("/news/?query=computer vision")
        self.assertEqual(response.status_code, 200)

        # Test that all object contain the required fields
        for news in response.json():
            self.assertTrue("headline" in news)
            self.assertTrue("link" in news)
            self.assertTrue("source" in news)

if __name__ == '__main__':
    unittest.main()