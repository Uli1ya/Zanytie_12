from vigenere import Vigenere
from encoders.caesar import Caesar

c = Caesar(5)
c.encode_to_file(input(),"MY_SECRET.txt")
c.decode_from_file("MY_SECRET.txt")
s = Caesar(5)
v = Vigenere("Привет")


print(s.encode("друг"))
print(v.encode("друг"))
#for i in range(34):
#    print(caesar.shift( "hellow", 1))

#print(caesar.encode("Hellow word!f"))
#print(caesar.decode("Khoorz zrug!"))
#print(vigenere.encode("Hellow", "word!"))
#print(vigenere.decode())