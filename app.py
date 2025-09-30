# Inicio del codigo.py

import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Dashboard de Datos Metereológicos", layout="wide")
st.title("Dashboard de Datos Metereológicos")
st.write("Visualización interactiva de datos metereológicos utilizando Streamlit y Plotly.")

conn = st.connection("mysql_db", type="sql")

@st.cache_data
def obtener_datos():
    # conn.query ejecuta la consulta y devuelve el resultado directamente como un DataFrame.
    # El argumento 'ttl' (Time To Live) es opcional. Le dice a Streamlit que vuelva a
    # ejecutar la consulta si los datos en caché tienen más de 10 minutos (600 segundos).
    df = conn.query("SELECT fecha, temperatura, humedad, presion FROM esp32_table_weather", ttl=600)
    return df

datos_df = obtener_datos()

st.subheader("Datos Metereológicos")
st.dataframe(datos_df)
st.subheader("Datos Temperatura")
fig_lineas_temp = px.line(datos_df, x='fecha', y=['temperatura','humedad'],
                     labels={'value': 'Valor', 'variable': 'Métrica'},
                     title='Evolución de Temperatura a lo Largo del Tiempo')

fig_lineas_temp.update_layout(height=500)
st.plotly_chart(fig_lineas_temp, use_container_width=True)
st.subheader("Datos Humedad")
fig_lineas_hum = px.line(datos_df, x='fecha', y=['humedad'],
                     labels={'value': 'Valor', 'variable': 'Métrica'},
                     title='Evolución de Humedad a lo Largo del Tiempo')
fig_lineas_hum.update_layout(height=500)
st.plotly_chart(fig_lineas_hum, use_container_width=True)