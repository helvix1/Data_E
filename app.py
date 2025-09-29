import pandas as pd
import streamlit as st
from datetime import datetime
from dotenv import load_dotenv
import os
import google.generativeai as genai

print("Librería GenAI cargada correctamente")


# Cargar variables de entorno desde .env
load_dotenv()

# Variables personalizadas
titulo = os.getenv("TITULO_APP", "Dashboard de Delitos")
municipio = os.getenv("MUNICIPIO_DESTACADO", "Medellín")
color = os.getenv("COLOR_PRINCIPAL", "#8C362E")

# Configuración inicial de la página
st.set_page_config(page_title=titulo, layout='wide')

# Estilos adaptables para móviles
st.markdown(f"""
    <style>
        .block-container {{
            padding: 1rem;
        }}
        h1 {{
            color: {color};
            text-align: center;
            font-size: 2rem;
        }}
        h3 {{
            color: {color};
            background-color: #FFF6F5;
            border: 2px solid #F2A88D;
            border-radius: 10px;
            padding: 10px;
            text-align: center;
            font-size: 1.1rem;
        }}
        @media (max-width: 768px) {{
            h1 {{
                font-size: 1.5rem;
            }}
            h3 {{
                font-size: 1rem;
            }}
        }}
    </style>
    <h1>{titulo}</h1>
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
st.write("📊 Análisis realizado por Elvis Moreno Osorio")
st.write("⚠️ Datos ficticios para propósitos educativos")
