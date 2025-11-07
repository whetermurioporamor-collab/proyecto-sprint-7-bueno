import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análisis Exploratorio de Datos")

df = pd.DataFrame({
    'Categoría': ['A', 'B', 'C'],
    'Valor': [10, 30, 20]
})

fig = px.bar(df, x='Categoría', y='Valor', title='Gráfico de barras')
st.plotly_chart(fig)
