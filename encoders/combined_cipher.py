from encoders.base_encoder import BaseEncoder
from encoders.common import shift

"""
To encode enter a string without commas. Another punctuation symbols are possible 
To decode enter a string. Delete commas and square brackets from the list.
"""

"""
Algorithm for this particular encoding:
1) If we have for encoding more than 1 word, we shuffle the sentence using shuffle_words_ind.
 (shuffle_words_ind parameter we get while initializing the class AnotherCipher object, by default it is equal 0)
2) We make inside shift in every word of the sentence we need to encode.This inside shift is as follows:
the word is splitted in halves. If the length of the word is an uneven number,then we take the first half as longer a longer one
 The first half of the word is reversed and shifted into the end of the word. The second part is also reversed and shifted into beginning of the word.
3) We use shift function from common.py module to make an alfabet shift for the copy of every word (with previosly shifted halves).
 The amount of shift for the copy is defined by key value that is assigned during initialization of the class object. Key doesn`t have a default value.
4) We encode the word with the help of its alfabetically shifted copy by xor encoding.
"""


class CombineCipher(BaseEncoder):
    _shuffle_words_ind = 0

    def __init__(self, key: int, shuffle_words_ind: int = 0):
        self.key = key
        self._shuffle_words_ind = shuffle_words_ind

    @property
    def shuffle_words_ind(self):
        return self._shuffle_words_ind

    @shuffle_words_ind.setter
    def shuffle_words_ind(self, new_shuffle_words_ind):
        self._shuffle_words_ind = new_shuffle_words_ind

    @staticmethod
    def shuffle_words(list_words: list = None, shuffle_words_ind: int = 0) -> list:
        if list_words == None:
            raise AttributeError('No text for encoding. An empty list of words was transmitted')
        else:
            return [list_words[(i + shuffle_words_ind) % len(list_words)] for i, word in enumerate(list_words)]

    @staticmethod
    def unshuffle_words(list_words: list = None, shuffle_words_ind: int = 0) -> list:
        if list_words == None:
            raise AttributeError('No text for encoding. An empty list of words was transmitted')
        else:
            return [list_words[(i - shuffle_words_ind) % len(list_words)] for i, word in enumerate(list_words)]

    @staticmethod
    def xor_encryption(word: str, shifted_new_word: str) -> str:
        xor_encrypted_word = ''
        print(word, 'xor!')
        print(shifted_new_word, 'xor!')
        for i in range(len(word)):
            xor_encrypted_word += chr(ord(word[i]) ^ ord(shifted_new_word[i]))
        return xor_encrypted_word

    @staticmethod
    def word_medium_shift(word: str) -> str:
        # word = 'koshka'
        if len(word) != 1:
            word_medium_ind = len(word) // 2 if len(word) % 2 else (len(word) // 2 - 1)
            part1 = word[: word_medium_ind:-1]
            part2 = word[word_medium_ind::-1]
            # print(part1+part2, 'debug')
            return part1 + part2
        return word

    @staticmethod
    def write_list(list_shifted_new_words, filename):
        with open(filename, "w", encoding="utf8") as f:
            f.write(' '.join(list_shifted_new_words))

    @staticmethod
    def read_list(filename: str):
        with open(filename, "r", encoding="utf8") as f:
            # print(f.read(), 'file')
            return f.read()

    def encode(self, text: str) -> str:
        list_words = list(text.split())

        shuffled_list_words = self.shuffle_words(list_words, self.shuffle_words_ind)

        list_shifted_new_words = []
        list_fully_encoded_words = []

        for word in shuffled_list_words:
            new_word = self.word_medium_shift(word)

            shifted_new_word = "".join(shift(ch, self.key) for ch in new_word)

            list_shifted_new_words.append(shifted_new_word)

            encoded_word = self.xor_encryption(new_word, shifted_new_word)
            list_fully_encoded_words.append(encoded_word)


        self.write_list(list_shifted_new_words, 'list_shifted_new_words.txt')


        return " ".join(list_fully_encoded_words)

    def decode(self, text: str) -> str:
        list_words_for_decoding = list(text.split(' '))

        str_shifted_new_words = self.read_list('list_shifted_new_words.txt')

        list_shifted_new_words = list(str_shifted_new_words.split())

        shuffled_sentence = []

        for words in list(zip(list_words_for_decoding, list_shifted_new_words)):

            xor_decrypted_word = self.xor_encryption(words[0], words[1])

            new_word_without_inner_shift = self.word_medium_shift(xor_decrypted_word)

            shuffled_sentence.append(new_word_without_inner_shift)

        unshuffled_sentence = self.unshuffle_words(shuffled_sentence, self.shuffle_words_ind)


        return ' '.join(unshuffled_sentence)