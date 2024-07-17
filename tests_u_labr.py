import unittest
import logging
import sys
from encoders import Caesar
from encoders import Vigenere
from encoders import MorseEncoder
from encoders import CombineCipher

CAESAR_CORRECT_KEYS = [1, 2, 3]
CAESAR_WRONG_KEYS = ["hello", 2.3]

VIGENERE_CORRECT_KEYS = ["hello", "привет"]
VIGENERE_WRONG_KEYS = ["12345",3, 10]

MORZE_CORRECT_KEYS = [None]

TEST_TEXTS = ["hello world", "Привет мир!", "ghjkl456321пролд"]
class KeyTests(unittest.TestCase):

    def test_caesar_key_validation(self):  # проверяет функционал шифра если создается ключ не корректный выдает ошибку
        for key in CAESAR_CORRECT_KEYS:
            test_caesar = Caesar(key)

        for key in CAESAR_WRONG_KEYS:
            try:
                test_caesar = Caesar(key)
            except AttributeError:
                pass
            else:
                raise AttributeError("Создали цезаря с некорректным ключем")


    def test_vigenere_key_validation(self):              # проверяет функционал шифра если создается ключ не корректный выдает ошибку
        for key in VIGENERE_CORRECT_KEYS:
            encoder = Vigenere(key)

        for key in VIGENERE_WRONG_KEYS:

            try:
                encoder = Vigenere(key)
            except AttributeError:
                pass
            else:
                raise AttributeError("Создали виженера с некорректным ключем")

class EncodeDecodeTests(unittest.TestCase):
    ENCODERS = [(Caesar, CAESAR_CORRECT_KEYS),
                (Vigenere, VIGENERE_CORRECT_KEYS),
                (MorseEncoder, MORZE_CORRECT_KEYS),
                (CombineCipher, [1, 2, 3])]

    def test_encode_decode(self):  # проверяет функционал декодера и  энкодера

        for Encoder, keys in self.ENCODERS:
            for key in keys:
                with self.subTest(f"Тестируем {Encoder} с ключем {key}"):

                    encoder = Encoder(key)
                    for text in TEST_TEXTS:
                        encoded_decoded_text = encoder.decode(encoder.encode(text))
                        self.assertEqual(text.lower(), encoded_decoded_text.lower(),"шифр не вернул изначальный текст")



