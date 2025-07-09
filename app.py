import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
car_data = pd.read_csv("vehicles_us (1).csv")

# Streamlit app title
st.title('Análisis Exploratorio de Datos de Anuncios de Venta de Coches')

# Display the first few rows of the dataset
st.subheader('Primeras filas del conjunto de datos')
st.dataframe(car_data.head())

# Histogram button
st.subheader('Visualización de Datos')
st.write('Seleccione una opción para visualizar los datos:')

hist_checkbox = st.checkbox('Construir histograma') # crear un botón
     
if hist_checkbox: # al hacer clic en el botón
"""esta sección del código crea un botón que, al hacer clic,
genera un histograma de la columna 'odometer' del conjunto de datos de anuncios de venta de coches.
El gráfico se muestra utilizando Plotly y Streamlit para una visualización interactiva."""

     # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
     # crear un histograma
    fig = px.histogram(car_data, x="odometer")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



#scatter button
st.subheader('Visualización de Datos')
st.write('Seleccione una opción para visualizar los datos:')

scatter_checkbox = st.checkbox('Construir Dispersión') # crear un botón
     
if scatter_checkbox: # al hacer clic en el botón
 """esta sección del código crea un botón que, al hacer clic,
genera un diagrama de dispersión de las columnas 'odometer' y 'price'"""

    # escribir un mensaje
    st.write('Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')
         
    # crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price")
     
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)    