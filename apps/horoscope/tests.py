from django.test import TestCase


class TestHoroscope(TestCase):
    def test_sign_elem(self):
        response = self.client.get("/horoscope/")
        self.assertEqual(response.status_code, 200)

    def test_sign_libra(self):
        response = self.client.get("/horoscope/libra")
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).", response.content.decode()
        )

    def test_sign_libra_redirect(self):
        response = self.client.get("/horoscope/7")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, "/horoscope/libra")


# Create your tests here.
