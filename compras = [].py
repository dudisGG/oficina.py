compras = []
item = input("item (fim para parar): ")
while item != "fim":
    compras.append(item)
    item = input("item(fim para parar): ")
print("sua lista:", compras)
print("total de itens:", len(compras)) 