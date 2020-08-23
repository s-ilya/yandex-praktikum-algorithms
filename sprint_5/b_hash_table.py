class HashTable:
    def __init__(self):
        self.__capacity = 1000
        self.__items = [None for _ in range(self.__capacity)]
        self.__not_found = -1

    def __hash(self, item: int) -> int:
        return item % self.__capacity

    def put(self, key: int, item: int) -> None:
        hash = self.__hash(key)
        hash_items = self.__items[hash] if self.__items[hash] is not None else list()

        updated_existing = False
        for index, key_value in enumerate(hash_items):
            if key_value[0] == key:
                hash_items[index] = (key_value[0], item)
                updated_existing = True
                break

        if not updated_existing:
            hash_items.append((key, item))

        self.__items[hash] = hash_items

    def get(self, key) -> int:
        hash = self.__hash(key)
        hash_items = self.__items[hash]

        if hash_items is None:
            return self.__not_found

        for key_value in hash_items:
            if key_value[0] == key:
                return key_value[1]

        return self.__not_found

    def delete(self, key) -> str:
        hash = self.__hash(key)
        hash_items = self.__items[hash]

        if hash_items is None:
            return 'error'

        for index, key_value in enumerate(hash_items):
            if key_value[0] == key:
                del hash_items[index]
                return 'ok'

        return 'error'


if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        n = int(input_txt.readline())
        hash_table = HashTable()

        for _ in range(n):
            input = input_txt.readline().strip().split(' ')
            command = input[0]
            key = int(input[1])

            if command == 'put':
                value = int(input[2])
                hash_table.put(key, value)
            elif command == 'get':
                output_txt.write(str(hash_table.get(key)) + '\n')
            elif command == 'delete':
                output_txt.write(hash_table.delete(key) + '\n')