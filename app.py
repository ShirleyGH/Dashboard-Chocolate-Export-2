import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URLs de los archivos CSV en tu repositorio (REEMPLAZA TU_USUARIO)
base_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-Chocolate-Export/main/"
clientes_url = base_url + "clientes.csv"
mercados_url = base_url + "mercados.csv"
exportaciones_url = base_url + "exportaciones.csv"
barreras_url = base_url + "barreras.csv"

# Cargar datos
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)

# Título
st.title("🌎 Dashboard Interactivo de Exportaciones de Chocolates")

# Filtro de país
paises = exportaciones["País"].unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises)

# Clientes
st.subheader("📋 Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)

# Exportaciones
st.subheader("📦 Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]

fig, ax = plt.subplots()
ax.bar(exportaciones_filtradas["País"], exportaciones_filtradas["Exportaciones (USD millones)"], color='#2E86C1')
ax.set_xlabel("País")
ax.set_ylabel("Exportaciones (USD millones)")
ax.set_title(f"Exportaciones de Chocolates en {pais_seleccionado}")
plt.xticks(rotation=45)
st.pyplot(fig)

# Segmentos de mercado
st.subheader("📊 Segmentos de Mercado")
mercados_filtrados = mercados[mercados["País"] == pais_seleccionado]
st.dataframe(mercados_filtrados)

# Barreras de entrada
st.subheader("🚧 Barreras de Entrada")
barreras_filtradas = barreras[barreras["País"] == pais_seleccionado]
st.dataframe(barreras_filtradas)

# Análisis comparativo
st.subheader("📈 Análisis Comparativo - Tamaños de Mercado")
fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.bar(mercados["País"], mercados["Tamaño del Mercado (USD millones)"], color='#F39C12')
ax2.set_xlabel("País")
ax2.set_ylabel("Tamaño del Mercado (USD millones)")
ax2.set_title("Comparación de Tamaños de Mercado")
plt.xticks(rotation=45)
st.pyplot(fig2)
