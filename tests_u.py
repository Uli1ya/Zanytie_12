from encoders import Caesar


CAESAR_CORRECT_KEYS = [1, 2, 3]
CAESAR_WRONG_KEYS = ["hello", 2.3]

TEST_TEXTS = ["hello world", "Привет мир!", "ghjkl456321пролд"]


def test_caesar_key_validation():  # проверяет функционал шифра если создается ключ не корректный выдает ошибку
    for key in CAESAR_CORRECT_KEYS:
        test_caesar = Caesar(key)
    for key in CAESAR_WRONG_KEYS:
        try:
            test_caesar = Caesar("hello")
        except AttributeError:
            pass
        else:
            raise AttributeError("Создали цезаря с некорректным ключем")





def test_caesar_encode_decode():        # проверяет функционал декодера и  энкодера
    key = 1
    encoder = Caesar(key)

    for text in TEST_TEXTS:
        if text.lower() != encoder.decode(encoder.encode(text)).lower():
            raise AttributeError("шифр не вернул изначальный текст")
        print(text.lower(), encoder.decode(encoder.encode(text)).lower())




test_caesar_key_validation()
test_caesar_encode_decode()
