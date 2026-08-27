#Hector Malaga Rodriguez 951 27/08/2026
#Gestionar el inventario de una tienda mediante diccionarios

productos = {1:{"nombre":"atun","precio":50,"cantidad_stock":10},
             2:{"nombre":"huevo","precio":3,"cantidad_stock":500},
             3:{"nombre":"leche","precio":32,"cantidad_stock":20},
             4:{"nombre":"pan","precio":120,"cantidad_stock":40},
             5:{"nombre":"sopa","precio":15,"cantidad_stock":66}}

def agregar_producto(id, nombre, precio, cantidad_stock):
    if id in productos:
        print(f"El id {id} ya existe, pongale otro")
    else:
        productos[id] = {"nombre": nombre,
                    "precio": precio,
                    "cantidad_stock": cantidad_stock}
        print("Producto agregado al almacen")

def editar_producto(id, nombre, precio, cantidad_stock):
    if not id in productos:
        print(f"El id {id} no existe, busque otro producto")
    else:
        productos[id]["nombre"] = nombre
        productos[id]["precio"] = precio
        productos[id]["cantidad_stock"] = cantidad_stock
    print("Producto editado")

def eliminar_producto(id):
    eliminado = productos.pop(id)
    print("El siguiente producto se elimino:", eliminado)

def vender(id, venta):
    if not id in productos:
        print(f"El id {id} no existe, busque otro producto")
    else:
        if productos[id]["cantidad_stock"] < venta:
            print("No hay inventario suficiente para la venta")
        else:
            productos[id]["cantidad_stock"] -= venta
            ganancias = venta * productos[id]["precio"]
            print(f"Producto vendido, se ganaron: ${ganancias} pesos")

def ver_inventario():
    print("Todo el inventario disponible:")
    for codigo,producto in productos.items():
        print("codigo", codigo)
        print("nombre", producto["nombre"])
        print("precio", producto["precio"])
        print("cantidad_stock", producto["cantidad_stock"])
        print("-----------------------------------------------")

if __name__ == "__main__":
     agregar_producto(5,"sal",45,85)
     agregar_producto(6,"sal",45,985)
     editar_producto(6,"sal",45,85)
     eliminar_producto(1)
     vender(4,10)
     ver_inventario()