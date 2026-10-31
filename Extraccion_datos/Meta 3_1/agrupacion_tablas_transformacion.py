#Hector Malaga Rodriguez 951 01/11/2026
import pandas as pd


# aqui creamos nuestra tabla ocn los productos de la tienda tal cual como esta en el documento y utilizando pandas para
# hacerlo un dataframe
def crear_datos():
    data = {
        "tienda":["A","A","A","B","B","B","C","C","C"],
        "producto":["manzana","platano","naranja","manzana","platano","naranja","manzana","platano","naranja"],
        "categoria":["fruta","fruta","fruta","fruta","fruta","fruta","fruta","fruta","fruta"],
        "precio":[30,20,35,25,30,45,35,20,25],
        "cantidad_vendida":[50,30,20,60,25,35,55,20,30],
        "calificacion":["A","B","C","A","B","A","C","B","A"],
    }
    df = pd.DataFrame(data)
    print(df)
    return df


# para asignar los codigos que se nos piden primero debemos tener un diccionario con los cambios que queremos realizar
# y luego con la funcion map podemos agregarlos en una coluna nueva o cambiar la que ya existe
def asignar_codigo(df: pd.DataFrame):
    codigo_tienda = {
        "A":1,
        "B":2,
        "C":3,
    }
    codigo_calificacion = {
        "A":3,
        "B":2,
        "C":1,
    }
    df["codigo_tienda"] = df["tienda"].map(codigo_tienda)
    df["codigo_calificacion"] = df["calificacion"].map(codigo_calificacion)

    print(df)
    return df


# para calcular las ventas totales por cada tienda utilizamos groupby para agrupar por tienda y luego seleccionamos
# la columna a aplicar una operación, en este caso la suma de ventas
def total_ventas(df: pd.DataFrame):
    total_vendidos = df.groupby("tienda").cantidad_vendida.sum().reset_index()
    print(total_vendidos)
    return total_vendidos


# para sacar el promedio de los precios de las tiendas, aplicamos lo mismo del punto anterior pero cambiando cantidad
# por precio y en vez de sumar ponemos promedio (mean) y redondeamos a 2 decimales
def precio_promedio(df: pd.DataFrame):
    promedios = df.groupby("tienda").precio.mean().round(2).reset_index()
    print(promedios)
    return promedios


# pandas cuenta con la funcion .pivot_table() que sirve como una tabla dinamica de excel, eneste caso lo usamos para ver
# que tantos productos se vedieron en cada tienda, agregando también la suma de las tiendas y de los productos
def cantidad_vendida_tiendas(df: pd.DataFrame):
    productos_tiendas = pd.pivot_table(
        data=df,
        values="cantidad_vendida",
        index="producto",
        columns="tienda",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="suma_total"
    )
    print(productos_tiendas)
    return productos_tiendas


# por ultimo tenemos de nuevo la funcion pivot_table pero esta vez para reflejar las ventas totales por productos
# de tienda, perooo como tal lafuncion no puede calcular operaciones dentro de ella por lo que debemos agregar una
# nueva columna a la tabla que calcule las ventas totales y luego si usarla en el pivote
def total_ventas_tienda_productos(df: pd.DataFrame):
    df["total_ventas"] = df["precio"] * df["cantidad_vendida"]
    total_ventas_cada_producto = pd.pivot_table(
        data=df,
        values="total_ventas",
        index="producto",
        columns="tienda",
        aggfunc="sum",
        fill_value=0,
        margins=True,
        margins_name="suma_total"
    )

    print(total_ventas_cada_producto)
    return total_ventas_cada_producto


# aqui llamamos a todas las funciones creadas
if __name__ == "__main__":
    df = crear_datos()
    print("===================================================")
    asignar_codigo(df)
    print("===================================================")
    total_ventas(df)
    print("===================================================")
    precio_promedio(df)
    print("===================================================")
    cantidad_vendida_tiendas(df)
    print("===================================================")
    total_ventas_tienda_productos(df)
    print(df)