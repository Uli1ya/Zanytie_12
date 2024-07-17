from encoders.base_encoder import BaseEncoder
import logging

class BinaryEncoder(BaseEncoder):
    def __init__(self,_key):
        super().__init__(_key)
    def encode(selfself,text: str):
        #logger = logging.getLogger()
        #logger.debug(self.encode(text))     #как встроить логер в код?
        return ' '.join(format(ord(char), '08b') for char in text)
    def decode(self, text: str):
        return ''.join(chr(int(char, 2)) for char in text.split())


key = 123

binary_encoder = BinaryEncoder(key)
text = input("любой текст")
binary_encoded = binary_encoder.encode(text)
print("зашифрованный текст")
print(binary_encoded)

decoded_text = binary_encoder.decode(binary_encoded)
print("зашифрованный текст")
print(binary_encoded)
print("дешифрованный текст")
print(decoded_text)


print(f"{__name__}")

if __name__ == "__main__":          #писать после принтов если хочется их импортировать не запуская при импорте, а чтобы они сохранились как функция
    print("меня не импортировали , меня запустили")