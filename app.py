import pandas as pd
import streamlit as st


url = 'https://github.com/helvix1/bootcamp_iafis/raw/refs/heads/main/datos_generales_ficticios.csv'
# Leer el archivo CSV con el separador correcto y la codificación adecuada
df = pd.read_csv(url, sep=";", encoding="utf-8")

# print(df.info)


#crear lista de columnas de interes
seleccion_columnas = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
# actualizo el dataframe -df- con las columnas de interes
df = df[seleccion_columnas].sort_values(by='FECHA_HECHOS', ascending=True).reset_index(drop=True)


#convierto la columna FECHA_HECHOS a tipo fecha
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce')
# xtraigo solo la fecha sin la hora
df['FECHA_HECHOS'] = df['FECHA_HECHOS'].dt.date

# CONFIGURAR LA PÁGINA Y EL TITULO DE LA APLICACIÓN
st.set_page_config(page_title="Dashboard de Datos de Delitos", layout="wide")
st.header("Análisis de Datos de Delitos")


#grafico de barras  para la columna DELITO
st.subheader("Distribución de Delitos")
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)

# Mostrar una sola vez el dataframe
st.dataframe(df)

# calculo de munciipos con más delitos
max_municipio = df['MUNICIPIO_HECHOS'].value_counts().index[0].upper()
st.write(f'Los municipios con más delitos son: {max_municipio}')

max_cantidad_municipio = df['MUNICIPIO_HECHOS'].value_counts().iloc[0]
#st.write(f'Con una cantidad de: {max_cantidad_municipio}') 

# CONSTRUIR LA PAGINA
st.set_page_config(page_title='Dashboard de Análisis de Delitos', layout='centered')
st.header('Dashboard de Análisis de Delitos')
#st.markdown(f"<center><h1>Dashboard de Análisis de Delitos</center>",

st.write(F"### Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} reportes")


# caculo de etapa mas frecuente
etapa_mas_frecuente = df['ETAPA'].value_counts().index[0]
#st.write(f'La etapa más frecuente en los delitos es: {etapa_mas_frecuente}')
cant_etapa_mas_frecuente = df['ETAPA'].value_counts().iloc[0]
st.write({etapa_mas_frecuente}, f'con una cantidad de: {cant_etapa_mas_frecuente}')

st.subheader(f"Municipio con más delitos: {max_municipio} con {max_cantidad_municipio} reportes")
st.subheader(f"Etapa más frecuente en los delitos: {etapa_mas_frecuente} con {cant_etapa_mas_frecuente} reportes")  

st.subheader('Comportamiento de los Delitos')
delitos = df['DELITO'].value_counts()
st.bar_chart(delitos)