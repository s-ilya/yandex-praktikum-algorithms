if __name__ == '__main__':
    with open('input.txt', mode='r') as input_txt, open('output.txt', mode='w') as output_txt:
        _ = int(input_txt.readline())
        words = input_txt.readline().strip().split(' ')
        anagrams = dict()

        for index, word in enumerate(words):
            word_hash = hash(''.join(sorted(word)))

            if word_hash not in anagrams:
                anagrams[word_hash] = [index]
            else:
                anagrams[word_hash].append(index)

        for anagram_indices in anagrams.values():
            output_txt.write(' '.join([str(n) for n in anagram_indices]) + '\n')
