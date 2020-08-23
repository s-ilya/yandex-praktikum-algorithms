from math import floor
from urllib.parse import urlsplit

__EMPTY_CODE = -1
__POST_METHOD = 'post'
__BASE = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def decode(code: str) -> int:
    if len(code) == 0:
        return __EMPTY_CODE

    decoded = 0

    for char in code:
        decoded = len(__BASE) * decoded + __BASE.find(char)

    return decoded


def encode(data: int) -> str:
    if data == __EMPTY_CODE:
        return ''

    if data == 0:
        return __BASE[0]

    encoded_parts_reversed = []
    while data > 0:
        encoded_parts_reversed.append(__BASE[data % len(__BASE)])
        data = floor(data / len(__BASE))

    return ''.join(reversed(encoded_parts_reversed))


class RequestsStorage:
    def __init__(self):
        self.__responses = []

    def get(self, url: str):
        n = self.__get_request_n(url)

        if n < len(self.__responses) and self.__responses[n][0] == url:
            return self.__responses[n][1]

        return 'error'

    @staticmethod
    def __get_request_n(url: str) -> int:
        parsed = urlsplit(url)
        parts = parsed.hostname.split('.')

        return decode(parts[0])

    def post(self, url: str, content: str) -> str:
        shortened_url = self.__get_shortened_url(len(self.__responses), url)

        self.__responses.append(
            (shortened_url, content)
        )

        return shortened_url

    @staticmethod
    def __get_shortened_url(n: int, url: str) -> str:
        parsed = urlsplit(url)
        parts = parsed.hostname.split('.')
        encoded_hostname = encode(n) + '.' + parts[1]

        return parsed.scheme + '://' + encoded_hostname


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n_requests = int(input_txt.readline())
        storage = RequestsStorage()

        for n_request in range(n_requests):
            request_parts = input_txt.readline().strip().split(' ')
            method = request_parts[0]
            url = request_parts[1]

            if method == __POST_METHOD:
                content = ' '.join(request_parts[2:])

                output_txt.write(storage.post(url, content) + '\n')
            else:
                output_txt.write(storage.get(url) + '\n')
