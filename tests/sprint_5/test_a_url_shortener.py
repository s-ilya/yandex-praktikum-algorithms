from unittest import TestCase

from sprint_5.a_url_shortener import decode, encode, RequestsStorage


class UrlShortenerTest(TestCase):
    def setUp(self) -> None:
        self.storage = RequestsStorage()

    def test_decode_empty(self):
        self.assertEqual(-1, decode(''))

    def test_decode_single(self):
        self.assertEqual(10, decode('a'))

    def test_decode_two(self):
        self.assertEqual(657, decode('aB'))

    def test_decode_first(self):
        self.assertEqual(0, decode('0'))

    def test_decode_sample(self):
        self.assertEqual(46777, decode('cat'))

    def test_encode_empty(self):
        self.assertEqual('', encode(-1))

    def test_encode_single(self):
        self.assertEqual('b', encode(11))

    def test_encode_first(self):
        self.assertEqual('0', encode(0))

    def test_encode_two(self):
        self.assertEqual('aC', encode(658))

    def test_encode_sample(self):
        self.assertEqual('cat', encode(46777))

    def test_get_empty(self):
        self.assertEqual('error', self.storage.get('http://0.com'))

    def test_post_single(self):
        self.assertEqual('http://0.com', self.storage.post('http://whatever.com', 'content'))

    def test_post_get_single(self):
        self.assertEqual('http://0.com', self.storage.post('http://whatever.com', 'content'))
        self.assertEqual('content', self.storage.get('http://0.com'))

    def test_post_get_unmatched(self):
        self.assertEqual('http://0.com', self.storage.post('http://whatever.com', 'content'))
        self.assertEqual('error', self.storage.get('http://0.ru'))

    def test_post_get_get(self):
        self.assertEqual('http://0.com', self.storage.post('http://whatever.com', 'content'))
        self.assertEqual('content', self.storage.get('http://0.com'))
        self.assertEqual('content', self.storage.get('http://0.com'))

    def test_post_get_multiple(self):
        self.assertEqual('https://0.com', self.storage.post('https://yandex.com', 'yandex content'))
        self.assertEqual('http://1.ru', self.storage.post('http://mail.ru', 'mail content'))
        self.assertEqual('yandex content', self.storage.get('https://0.com'))
        self.assertEqual('mail content', self.storage.get('http://1.ru'))

    def test_post_get_some_unmatched(self):
        self.assertEqual('https://0.com', self.storage.post('https://yandex.com', 'yandex content'))
        self.assertEqual('http://1.ru', self.storage.post('http://mail.ru', 'mail content'))
        self.assertEqual('yandex content', self.storage.get('https://0.com'))
        self.assertEqual('error', self.storage.get('https://1.com'))