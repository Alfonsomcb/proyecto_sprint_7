# proyecto_sprint_7
# Aplicación Web para el Análisis Exploratorio de Datos de Venta de Coches

## 📜 Descripción del Proyecto

Esta es una aplicación web interactiva construida con **Streamlit** para realizar un análisis exploratorio de datos (EDA) sobre un conjunto de datos de anuncios de venta de coches en Estados Unidos.

La aplicación permite a los usuarios cargar y visualizar el conjunto de datos y generar gráficos interactivos para explorar la relación entre diferentes variables, como el kilometraje (odómetro) y el precio de los vehículos.

## ✨ Características

La aplicación cuenta con las siguientes funcionalidades:

* **Visualización del DataFrame**: Muestra las primeras filas del conjunto de datos para una inspección rápida.
* **Histograma Interactivo**: Mediante una casilla de verificación, el usuario puede generar un histograma de la columna `odometer` para analizar la distribución del kilometraje de los coches.
* **Gráfico de Dispersión Interactivo**: Ofrece una segunda opción para crear un diagrama de dispersión que explora la relación entre el kilometraje (`odometer`) y el precio (`price`) de los vehículos.
* **Interactividad**: Todos los gráficos son generados con Plotly, lo que permite a los usuarios hacer zoom, desplazarse y obtener información detallada al pasar el cursor sobre los datos.

## 💻 Tecnologías Utilizadas

* **Lenguaje**: Python 3
* **Librerías**:
    * `Streamlit`: Para la creación y despliegue de la aplicación web.
    * `Pandas`: Para la carga y manipulación de los datos.
    * `Plotly Express`: Para la generación de visualizaciones interactivas.

## 🚀 Cómo Ejecutar la Aplicación

Para ejecutar esta aplicación en tu entorno local, sigue estos pasos:

1.  **Clona o descarga este repositorio.**

2.  **Asegúrate de tener el conjunto de datos**: El archivo `vehicles_us (1).csv` debe estar en la misma carpeta que el script `app.py`.

3.  **Instala las dependencias**: Abre una terminal o línea de comandos y ejecuta el siguiente comando para instalar las librerías necesarias:
    ```bash
    pip install streamlit pandas plotly
    ```

4.  **Ejecuta la aplicación**: En la misma terminal, navega hasta la carpeta del proyecto y ejecuta:
    ```bash
    streamlit run app.py
    ```

5.  La aplicación se abrirá automáticamente en tu navegador web.


