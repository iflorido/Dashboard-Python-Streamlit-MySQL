import streamlit as st
import _mysql_connector

@st.cache_resource
def conectar_mysql():
    return _mysql_connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="tu_base_de_datos"
    )