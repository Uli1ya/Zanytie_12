from common import shift
from encoders.base_encoder import BaseEncoder


class Test_my_shifr(BaseEncoder):
 #   @BaseEncoder.key.setter
 #   def key(self, new_key: int):
  #      if not isinstance(new_key, int):
 #           raise AttributeError(f'Ключом может быть только целое число, но передан "{new_key}"')
 #       self._key = new_key

    def encode(self, text: str) -> str:

        return f"{ord(text) - 96}"


    def decode(self, text: str) -> str:
     return f"{chr(text)+96}"

v = "друг"
s = '\xd0\xb4\xd1\x80\xd1\x83\xd0\xb3'
print(v.encode())
print(s.decode())