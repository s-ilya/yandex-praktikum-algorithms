if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        cypher = input_txt.readline().strip()
        words_n = int(input_txt.readline())

        words = {}
        for _ in range(words_n):
            words[input_txt.readline().strip()] = 0

        for char in cypher:
            for (word, char_index) in words.items():
                if char_index == len(word):
                    continue

                if word[char_index] == char:
                    words[word] += 1

        result = ''
        for (word, char_index) in words.items():
            if char_index == len(word) and (len(word) > len(result) or (len(word) == len(result) and word < result)):
                result = word

        output_txt.write(result)
