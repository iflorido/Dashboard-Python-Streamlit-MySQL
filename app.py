# Inicio del codigo.py

import streamlit as st
import plotly.express as px
import _mysql_connector
from conexion_mysql import conectar_mysql

st.set_page_config(page_title="Dashboard de Datos Metereológicos", layout="wide")
st.title("Dashboard de Datos Metereológicos")
st.write("Visualización interactiva de datos metereológicos utilizando Streamlit y Plotly.")

''' Este es el contenido de conexion_mysql.py 

@st.cache_resource
def conectar_mysql():
    return _mysql_connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )
      
'''