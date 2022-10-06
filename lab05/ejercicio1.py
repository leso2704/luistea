ch = "X-DSPAM-Confidence:0.8475"

pos1 = ch.find(":")
print("Inicia en : "+ str(pos1))

pos2 = ch.find("5")
print("Fnaliza en: "+ str(pos2))

final = len(ch)
substring = ch[pos1+1:final]
valor = float(substring)

print(valor)
print(type(valor))