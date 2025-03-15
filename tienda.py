



lista_producto = [
    {"id":1 ,"nombre":"pantalon" , "precio":60000 ,"stock":30},
    {"id":2 ,"nombre":"camisilla" , "precio":20000,"stock":34},
    {"id":3 ,"nombre":"camisa" , "precio":50000,"stock":45}

]

lista_pedidos = [
    {"id_pedidos":101 ,"cliente":"cliente1" , "producto":[1,2] ,"estado":"en proceso"},
    {"id_pedidos":124 ,"cliente":"clente2" , "producto":[3],"estado":"en proceso"},
  
]

cliente_registrado = [
 {"nombre":"cliente1","email":"cliente1@gmail.com" , "producto":[1,2] ,"direccion":"calle-14-carrera-112"},
 {"nombre":"cliente2" ,"cliente":"clente2@gmail.com" , "producto":[3],"direccion":"calle-34-carrera-12"},


]

nuevo_producto = {"id": 4, "nombre": "bermudas", "precio": 70000, "stock": 220} 
lista_producto.append(nuevo_producto) 

for pedidos in lista_pedidos :
    if pedidos["id_pedidos"] == 101 :
        pedidos["estado"]="entregado"




def encontrar_pedidos_por_email(email):
    return [pedido for pedido in lista_pedidos if pedido["cliente"] == email]


print("\nLista de productos actualizada:")
for producto in lista_producto:
    print(producto)

print("\nLista de pedidos actualizada:")
for pedido in lista_pedidos:
    print(pedido)

print("\nClientes registrados:")
for cliente in cliente_registrado:
    print(cliente)


