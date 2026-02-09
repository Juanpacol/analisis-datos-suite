import streamlit as st
import pandas as pd
from streamlit_extras.metric_cards import style_metric_cards

def show_data_preview(df):
    """
    Shows a preview of the dataframe (head).
    """
    st.subheader("Vista Previa de Datos")
    st.dataframe(df.head())

def show_data_info(df):
    st.subheader("Resumen Ejecutivo")
    
    # Creamos tres columnas para las tarjetas
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total de Registros", value=df.shape[0])
    with col2:
        st.metric(label="Total de Columnas", value=df.shape[1])
    with col3:
        nulos = df.isnull().sum().sum()
        st.metric(label="Valores Nulos", value=nulos, delta="¡Cuidado!" if nulos > 0 else "Limpio")

    # Esto le da el diseño profesional (sombras y bordes)
    style_metric_cards(border_left_color="#3e82f7")

    st.markdown("---")
    st.markdown("**Análisis de Estructura:**")
    summary_df = pd.DataFrame({
        'Tipo': df.dtypes.astype(str),
        'Vacíos': df.isnull().sum(),
        'Únicos': df.nunique()
    })
    st.dataframe(summary_df, use_container_width=True)

def show_statistics(df):
    """
    Shows descriptive statistics for numerical columns.
    """
    st.subheader("Estadísticas Descriptivas")
    if not df.select_dtypes(include=['number']).empty:
        st.dataframe(df.describe())
    else:
        st.info("No hay columnas numéricas para mostrar estadísticas.")
