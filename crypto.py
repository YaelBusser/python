phrase = input("Ecrivez une phrase à crypter : ")
for i in range(len(phrase)):
    if phrase[i] == "z" or phrase[i] == "Z":
        ok = int(ord(phrase[i]))
        ok -= 25
        ok = chr(ok)
    else:
        ok = int(ord(phrase[i]))
        ok += 1
        ok = chr(ok)
    print(ok) 