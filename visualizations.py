import streamlit as st
import plotly.express as px
import pandas as pd

def plot_data(df):
    st.subheader("Visualización Adaptativa")
    
    if df.empty:
        st.info("No hay datos para mostrar.")
        return

    selected_col = st.selectbox("Selecciona una columna:", df.columns)
    
    # 1. DETECCIÓN DE TIPO
    is_numeric = pd.api.types.is_numeric_dtype(df[selected_col])
    
    if is_numeric:
        # --- SOLO MUESTRA ESTO SI ES NÚMERO ---
        st.info(f"Analizando datos numéricos de: {selected_col}")
        fig = px.histogram(df, x=selected_col, nbins=20, 
                           title=f"Distribución de {selected_col}")
        fig.update_traces(marker_line_width=1.5, marker_line_color="white")
        fig.update_layout(bargap=0.1)
        st.plotly_chart(fig, use_container_width=True)
        
    else:
        # --- SOLO MUESTRA ESTO SI ES TEXTO (OBJECT/STRING) ---
        st.info(f"Analizando categorías de: {selected_col}")
        
        # Preparamos los datos: contamos frecuencias
        conteo = df[selected_col].value_counts().reset_index()
        conteo.columns = [selected_col, 'Frecuencia']
        
        # Permitimos al usuario elegir el tipo de gráfico para texto
        tipo_grafico = st.radio("Formato visual:", ["Barras", "Tarta", "Treemap"], horizontal=True)
        
        if tipo_grafico == "Barras":
            fig = px.bar(conteo.head(15), x=selected_col, y='Frecuencia', 
                         color='Frecuencia', title=f"Top 15: {selected_col}")
            fig.update_traces(marker_line_width=1, marker_line_color="white")
            
        elif tipo_grafico == "Tarta":
            fig = px.pie(conteo.head(10), names=selected_col, values='Frecuencia', 
                         title=f"Distribución de {selected_col}")
            
        else: # Treemap
            fig = px.treemap(conteo.head(20), path=[selected_col], values='Frecuencia',
                             title=f"Mapa de árbol de {selected_col}")

        st.plotly_chart(fig, use_container_width=True)