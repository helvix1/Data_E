import pandas as pd
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Variables personalizadas
titulo = os.getenv("TITULO_APP", "Dashboard de Delitos")
municipio = os.getenv("MUNICIPIO_DESTACADO", "Medellín")
color = os.getenv("COLOR_PRINCIPAL", "#8C362E")

# Configuración inicial de la página
st.set_page_config(page_title=titulo, layout='wide')

# Encabezado personalizado
st.markdown(f"""
    <h1 style='color:{color}; text-align:center;'>{titulo}</h1>
    <style>
        .block-container {{
            padding: 3rem 2rem 2rem 2rem;
            max-width: 1200px;
        }}
        h3 {{
            color: {color};
            background-color: #FFF6F5;
            border: 2px solid #F2A88D;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
        }}
    </style>
""", unsafe_allow_html=True)

# Imagen del encabezado
st.image('img/Dashboard_fiscalia.png', width='stretch')

# Cargar datos desde GitHub
url = 'https://github.com/helvix1/bootcamp_iafis/raw/refs/heads/main/datos_generales_ficticios.csv'
df = pd.read_csv(url, sep=";", encoding="utf-8")

# Columnas de interés
columnas_interes = ['FECHA_HECHOS', 'DELITO', 'ETAPA', 'FISCAL_ASIGNADO', 'DEPARTAMENTO', 'MUNICIPIO_HECHOS']
df = df[columnas_interes].copy()

# Convertir fechas
df['FECHA_HECHOS'] = pd.to_datetime(df['FECHA_HECHOS'], errors='coerce').dt.date

# Ordenar por fecha
df.sort_values(by='FECHA_HECHOS', ascending=True, inplace=True)
df.reset_index(drop=True, inplace=True)

# Métricas principales
municipio_top = df['MUNICIPIO_HECHOS'].value_counts().idxmax().upper()
cantidad_municipio_top = df['MUNICIPIO_HECHOS'].value_counts().max()
etapa_top = df['ETAPA'].value_counts().idxmax()
cantidad_etapa_top = df['ETAPA'].value_counts().max()

# Mostrar métricas en columnas
col1, col2 = st.columns(2)
with col1:
    st.markdown(f"<h3>Municipio con más delitos: {municipio_top} ({cantidad_municipio_top} reportes)</h3>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<h3>Etapa más frecuente: {etapa_top} ({cantidad_etapa_top} registros)</h3>", unsafe_allow_html=True)

# Gráfico de delitos
st.subheader("📊 Distribución de Delitos")
delitos = df['DELITO'].value_counts().sort_values()
st.bar_chart(delitos)

# Mostrar tabla
st.subheader("📋 Datos procesados")
st.dataframe(df)

# Pie de página
st.markdown("---")
st.write("📊 Análisis realizado por Helvix")
st.write("⚠️ Datos ficticios para propósitos educativos")







#st.markdown("<h1>TITULO</h1>", unsafe_allow_html=True)