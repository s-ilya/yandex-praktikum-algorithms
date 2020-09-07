from unittest import TestCase
from urllib.parse import urlsplit
from random import choice
from RandomWordGenerator import RandomWord

from a_url_shortener import RequestsStorage, decode, encode


class RequestsStorageWorking:
    def __init__(self):
        self.__responses = dict()

    def get(self, url: str):
        return self.__responses[url] if url in self.__responses else 'error'

    def post(self, url: str, content: str) -> str:
        shortened_url = self.__get_shortened_url(len(self.__responses), url)
        self.__responses[shortened_url] = content

        return shortened_url

    @staticmethod
    def __get_shortened_url(n: int, url: str) -> str:
        parsed = urlsplit(url)
        parts = parsed.hostname.split('.')
        encoded_hostname = encode(n) + '.' + parts[1]

        return parsed.scheme + '://' + encoded_hostname


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

    def test_post_get_unmatched_zone(self):
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

    def test_unmatched_scheme(self):
        self.assertEqual('https://0.com', self.storage.post('https://domain.com', 'content'))
        self.assertEqual('error', self.storage.get('http://0.com'))

    def test_random_encode_decode(self):
        BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        def lib_encode(num):
            """Encode a positive number into Base X and return the string.

            Arguments:
            - `num`: The number to encode
            - `alphabet`: The alphabet to use for encoding
            """
            if num == 0:
                return BASE62[0]
            arr = []
            arr_append = arr.append  # Extract bound-method for faster access.
            _divmod = divmod  # Access to locals is faster.
            base = len(BASE62)
            while num:
                num, rem = _divmod(num, base)
                arr_append(BASE62[rem])
            arr.reverse()
            return ''.join(arr)

        def lib_decode(string):
            """Decode a Base X encoded string into the number

            Arguments:
            - `string`: The encoded string
            - `alphabet`: The alphabet to use for decoding
            """
            base = len(BASE62)
            strlen = len(string)
            num = 0

            idx = 0
            for char in string:
                power = (strlen - (idx + 1))
                num += BASE62.index(char) * (base ** power)
                idx += 1

            return num

        for n in range(10000):
            lib_encoded = lib_encode(n)
            my_encoded = encode(n)

            self.assertEqual(lib_encoded, my_encoded, msg='Error encoding {}'.format(n))

            lib_decoded = lib_decode(lib_encoded)
            my_decoded = decode(lib_encoded)

            self.assertEqual(lib_decoded, my_decoded, msg='Error decoding {}'.format(lib_decoded))

    def test_random_storage(self):
        random_words = RandomWord(3)
        storage = RequestsStorage()
        storage_ok = RequestsStorageWorking()

        urls = list()
        methods = ['get', 'post']
        commands = list()

        def new_random_url():
            scheme = ['http', 'https', 'ftp']

            url = '{}://{}.{}'.format(
                choice(scheme), random_words.generate(), random_words.generate()
            )

            return url if url not in urls else new_random_url()

        for _ in range(90000):
            method = choice(methods)

            if method == 'get':
                should_request_existing = choice([True, False])
                url = choice(urls) if should_request_existing and len(urls) > 0 else new_random_url()
                commands.append('get {}'.format(url))

                self.assertEqual(storage_ok.get(url), storage.get(url), msg='\n'.join(commands))
            else:
                url = new_random_url()
                content = ' '.join(random_words.getList(num_of_words=3))

                urls.append(url)
                commands.append('post {} {}'.format(url, content))

                self.assertEqual(storage_ok.post(url, content), storage.post(url, content), msg='\n'.join(commands))
