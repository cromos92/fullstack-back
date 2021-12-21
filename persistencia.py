""" declara variables para guardar un pedido"""
def guardar_pedido(nombre,apellidos):
    """ escribre en un archivo txt variables"""
    with open("pedidos.txt", "a", encoding="utf-8") as file:
        file.write(nombre + " " + apellidos + ",\n")
        file.close()
        