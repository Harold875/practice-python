my_list = [1, 2]

# append() -> agrega el elemento al final
my_list.append(3)
print(my_list)

print(my_list[0])

my_list[0] = 0
print(my_list)

# insert() -> Agrega el elemento en un indice especifico
my_list.insert(1, 1)
print(my_list)

# pop() -> elimina elemento, por defecto el ultimo, si se le pasa el indice eliminara el elemento del indice
my_list.pop()
print(my_list)
