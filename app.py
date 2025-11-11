import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


st.title("Análisis Exploratorio de Datos")

# Leer los datos del archivo CSV
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Crear un histograma utilizando plotly.graph_objects
# Se crea una figura vacía y luego se añade un rastro de histograma
fig = px.histogram(car_data, x='odometer', title='Distribución del Odómetro')

st.plotly_chart(fig)

st.set_page_config(page_title="Cuadro de Mandos", layout="wide")

st.header("📊 Cuadro de Mandos: Análisis de Vehículos Usados")

car_data = pd.read_csv('notebooks/vehicles_us.csv')

if st.button('Construir histograma'):
    st.write('🔍 Creación de un histograma para la columna "odometer"')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)
if st.button('Construir gráfico de dispersión'):
    st.write('🔍 Creación de un gráfico de dispersión entre "odometer" y "price"')
    fig = px.scatter(car_data, x='odometer', y='price', title='Relación entre Odómetro y Precio')
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar histograma de odómetro'):
    st.write('🔍 Histograma de la columna "odometer"')
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig.update_layout(title_text='Distribución del Odómetro')
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar gráfico de dispersión odómetro vs precio'):
    st.write('🔍 Dispersión entre "odometer" y "price"')
    fig = px.scatter(car_data, x='odometer', y='price', title='Relación entre Odómetro y Precio')
    st.plotly_chart(fig, use_container_width=True)
