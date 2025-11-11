import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis Exploratorio de Datos")

# Leer los datos del archivo CSV
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Crear un histograma utilizando plotly.graph_objects
# Se crea una figura vacía y luego se añade un rastro de histograma
fig = px.histogram(car_data, x='odometer', title='Distribución del Odómetro')

st.plotly_chart(fig)
