import sha3

def MyHash(texte):
    print("le code hash de \"",texte,"\" avec sha3 est: ", sha3.hash(texte))

mytest = "toto titi tata"
MyHash(mytest)


