#Hector Malaga Rodriguez 951 26/09/2026
#Trabajos de la meta 2.2
import pandas as pd
import numpy as np
from typing import List

#descripción: función que reciba como parámetro un DataFrame y retorne el porcentaje de valores nulos de cada columna.
def porcentaje_valores_nulos(df: pd.DataFrame):
    nulos = df.isnull().mean() * 100
    return nulos


#función que reciba como parámetro un DataFrame y retorne el número de renglones duplicados.
def numero_renglones_duplicados(df: pd.DataFrame):
    duplicados = df.duplicated().sum()
    return duplicados


#función que reciba como parámetro un DataFrame y un máximo porcentaje. Este debe eliminar todas las columnas que superen o igualen el máximo porcentaje de valores
#nulos establecidos en el DataFrame Original. Retornar la lista nombres de columnas eliminadas. Validar que el porcentaje máximo esté entre 0 y 1.
def eliminar_mayores_porcentajes(df: pd.DataFrame, porcentaje):
    if not (0.0 <= porcentaje <= 1.0):
        raise ValueError("El porcentaje debe estar entre 0 y 1")
    promedio_nulos = df.isnull().mean()
    columnas_eliminadas = promedio_nulos[promedio_nulos >= porcentaje].index.tolist()
    df.drop(columns=columnas_eliminadas, inplace=True)

    return columnas_eliminadas


#función que reciba como parámetro un DataFrame, una lista con los nombres de las columnas a verificar y una cadena. La cadena solo puede ser mean, bfill o ffill,
#en caso contrario lanzar una excepción. Debe sustituir los valores nulos por el metodo especificado y retornar del dataframe duplicado
def sustituir_valores_nulos(df: pd.DataFrame, lista, cadena):
    metodos_validos = ["mean", "bfill", "ffill"]
    if cadena not in metodos_validos:
        raise ValueError(f"Método '{cadena}' no válido. Opciones permitidas: {metodos_validos}")

    for col in lista:
        if col in df.columns:
            if cadena == "mean":
                if pd.api.types.is_numeric_dtype(df[col]):
                    promedio = df[col].mean()
                    df[col] = df[col].fillna(promedio)
                else:
                    raise TypeError(
                        f"No se puede aplicar 'mean' a la columna no numérica '{col}'."
                    )
            elif cadena == "bfill":
                df[col] = df[col].bfill()
            elif cadena == "ffill":
                df[col] = df[col].ffill()

    return df


#función que reciba como parámetro un DataFrame y elimine los renglones repetidos en el DataFrame Original. Debe retornar la cantidad de renglones eliminados.
def renglones_eliminados(df: pd.DataFrame):
    total_inicial = len(df)
    df.drop_duplicates(inplace=True)
    total_final = len(df)
    eliminados = total_inicial - total_final

    return eliminados


if __name__ == "__main__":
    datos = {
        "nombre": ["Juan", "Kevin", "Hector", "Ana", "Ana", "Charly"],
        "edad": [20, np.nan, 21, 25, 25, 20],
        "pais": ["MX", np.nan, "USA", "MX", "MX", "USA"],
        "columna_vacia": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan]
    }
    lista = ["edad","pais"]
    dataframe = pd.DataFrame(datos)
    print(dataframe)
    print("porcentajes valores nulos\n",porcentaje_valores_nulos(dataframe))
    print("\n\nnumero de renglones duplicados encontrados:\n",numero_renglones_duplicados(dataframe))
    print("\n\nColunas eliminadas en base al porcentaje de nulos:\n",eliminar_mayores_porcentajes(dataframe,0.5))
    print("\n\nDataframe modificado:\n",sustituir_valores_nulos(dataframe,lista,"ffill"))
    print("\n\nCantidad de reglones eliminados: \n",renglones_eliminados(dataframe))