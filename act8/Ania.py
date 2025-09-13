import pandas as pd
import numpy as np
import os


# a) Carga de archivos (csv, xlsx, html y json) a DataFrames
def cargar_dataset(ruta_archivo):
    extension = os.path.splitext(ruta_archivo)[1].lower()

    if extension == ".csv":
        return pd.read_csv(ruta_archivo)
    elif extension in [".xlsx", ".xls"]:
        return pd.read_excel(ruta_archivo)
    elif extension == ".json":
        return pd.read_json(ruta_archivo)
    elif extension == ".html":
        return pd.read_html(ruta_archivo)
    else:
        raise ValueError("error formato no soportado")
    
"""
Obtener la extensión del archivo con os.path.splitext().
Convertir la extensión a minúsculas para evitar errores.
Si es .csv, cargar con pd.read_csv().
Si es .xlsx o .xls, cargar con pd.read_excel().
Si es .json, cargar con pd.read_json().
Si es .html, cargar con pd.read_html() (devuelve lista de tablas).
Si no coincide, lanzar un ValueError("error formato no soportado").
"""

# b) Sustitución de valores nulos con ffill
def nulos_ffill(df):
    return df.fillna(method="ffill")
"""
Recibir el DataFrame.
Llamar a fillna(method="ffill")
Sustituye cada valor nulo por el último valor válido encontrado antes de ese punto.
Devuelve el DataFrame modificado.
"""

# c) Sustitución de valores nulos con bfill
def nulos_bfill(df):
    return df.fillna(method="bfill")

"""
Recibir el DataFrame.
Llamar a fillna(method="bfill")
Sustituye cada valor nulo por el siguiente valor válido encontrado después de ese punto.
Devuelve el DataFrame modificado.
"""

# d) Sustitución de nulos en variables string por un valor fijo
def nulos_string(df, valor="Desconocido"):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="object").columns:
        df_copy[col] = df_copy[col].fillna(valor)
    return df_copy
"""
Crear una copia del DataFrame para no modificar el original.
Seleccionar las columnas de tipo object (strings) con select_dtypes(include="object").
Iterar sobre cada columna de ese tipo.
Reemplazar sus nulos con el valor fijo de desconocido.
Devolver el nuevo DataFrame.
"""
# e) Sustitución de nulos por promedio
def nulos_prom_df(df):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="number").columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
    return df_copy
"""
Crear copia del DataFrame.
Seleccionar columnas numéricas (include="number").
Iterar columna por columna.
Calcular el promedio (mean()) de la columna.
Rellenar sus nulos con ese promedio.
Devolver DataFrame.
"""

# f) Sustitución de nulos por mediana
def nulos_median_df(df):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="number").columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy
"""
Crear copia del DataFrame.
Seleccionar columnas numéricas.
Iterar sobre cada columna.
Calcular la mediana.
Sustituir nulos por esa mediana.
Devolver el DataFrame.
"""
# g) Sustitución de nulos por constante
def nulos_constante_df(df, constante=0):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="number").columns:
        df_copy[col] = df_copy[col].fillna(constante)
    return df_copy
"""
Crear copia del DataFrame.
Seleccionar columnas numéricas.
Iterar columna por columna.
Rellenar sus nulos con el valor de la constante de 0.
Devolver DataFrame
"""
# i) Identificación de valores nulos
def identificar_nulos(df):
    import pandas as pd
    from IPython.display import display  # para usar display en notebooks

    nulos_columna = df.isnull().sum()
    total_nulos = df.isnull().sum().sum()
    porcentaje_nulos = (df.isnull().mean() * 100).round(2)

    resumen = pd.DataFrame({
        "Nulos": nulos_columna,
        "Porcentaje": porcentaje_nulos
    })
    display(
        resumen.sort_values(by="Porcentaje", ascending=False)
               .style.format({'Porcentaje': "{:.2f}%"})
    )

    return resumen, f"Total de valores nulos {total_nulos}"
"""
Calcular cantidad de nulos por columna con df.isnull().sum().
Calcular cantidad total de nulos en todo el DataFrame (.sum().sum()).
Calcular porcentaje de nulos por columna (df.isnull().mean()*100).round(2).
Crear un DataFrame resumen con columnas Nulos y Porcentaje.
Ordenar de mayor a menor por porcentaje.
Mostrarlo con display() en formato de tabla con %.2f% para redondear.
Devolver el resumen y el total de nulos.
"""
# j) 
def string(df):
    df_copy = df.copy()
    object = df_copy.select_dtypes(include="object").columns
    return object