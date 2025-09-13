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

# b) Sustitución de valores nulos con ffill
def nulos_ffill(df):
    return df.fillna(method="ffill")

# c) Sustitución de valores nulos con bfill
def nulos_bfill(df):
    return df.fillna(method="bfill")

# d) Sustitución de nulos en variables string por un valor fijo
def nulos_string(df, valor="Desconocido"):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="object").columns:
        df_copy[col] = df_copy[col].fillna(valor)
    return df_copy

# e) Sustitución de nulos por promedio
def nulos_prom_df(df):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="number").columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].mean())
    return df_copy

# f) Sustitución de nulos por mediana
def nulos_median_df(df):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="number").columns:
        df_copy[col] = df_copy[col].fillna(df_copy[col].median())
    return df_copy

# g) Sustitución de nulos por constante
def nulos_constante_df(df, constante=0):
    df_copy = df.copy()
    for col in df_copy.select_dtypes(include="number").columns:
        df_copy[col] = df_copy[col].fillna(constante)
    return df_copy

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

# j) 
def string(df):
    df_copy = df.copy()
    object = df_copy.select_dtypes(include="object").columns:
    return object