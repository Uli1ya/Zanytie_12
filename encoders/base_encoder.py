from abc import ABC, abstractmethod
import logging

class BaseEncoder(ABC):
    _key = None

    def __init__(self, key):
        self.key = key

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, new_key):
        self._key = new_key

    @abstractmethod
    def encode(self, text: str, key):
        pass

    @abstractmethod
    def decode(self, text: str, key):
        pass

    def encode_to_file(self, text: str, filename: str):

        with open(filename, "w") as f:
            logger = logging.getLogger()               # возвращает объект логера запросит логер который существует
            logger.debug(self.encode(text))
            f.write(self.encode(text))

    def decode_from_file(self,  filename: str) -> str:
        with open(filename, "r", encoding="utf8") as f:
            return self.decode(f.read())



