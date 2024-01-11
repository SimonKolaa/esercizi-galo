num = int(input("Inserisci un numero decimale: "))

bit_list = []

while num > 0:
    bit_list.append(num % 2)
    num //= 2
print("Conversione binaria: ", end="")
for bit in reversed(bit_list):
    print(bit, end="")
