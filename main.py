import encoders


a = encoders.test_morze.MorseEncoder()

#print(a.encode("друг"))
#c = encoders.Caesar(5)
a.encode_to_file(input(),"MY_SECRET.txt")
#print(a.encode_to_file("MY_SECRET.txt"))
print(a.decode_from_file("MY_SECRET.txt"))
#v = encoders.Vigenere("Привет")



#print(v.encode("друг"))
#for i in range(34):
#print(caesar.shift( "hellow", 1))

#print(caesar.encode("Hellow word!f"))
#print(caesar.decode("Khoorz zrug!"))

#print(vigenere.decode())