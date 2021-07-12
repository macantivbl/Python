class superList(list):
    def __len__(self):
        return 1000
    pass


super_lista1 = superList();

x = len(super_lista1)
print(x)
super_lista1.append(5)
x = super_lista1[0]
print(x)