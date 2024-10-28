import unittest
from webapp import app  

class BasicTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Test istemcisini oluştur
        cls.client = app.test_client()
        app.config['TESTING'] = True

    def test_home_page(self):
        # Ana sayfaya erişim testi
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)  # 200 yanıt kodunu bekleriz

    def test_login_page(self):
        # Login sayfasına erişim testi
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)  # 200 yanıt kodunu bekleriz

if __name__ == "__main__":
    unittest.main()