n_valori = int(input("numero valori"))
my_list=[]
media=0
for i in range(n_valori):
    my_list.append(i)
print(my_list)
for o in range(n_valori):
    media+=my_list[o]
media=media/n_valori
print(f"media {media}") 
minimo=my_list[0]   
massimo=my_list[-1]
print(f"minimo{minimo}")
print(f"massimo{massimo}")