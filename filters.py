import streamlit as st
import pandas as pd

def filter_dataframe(df):
    """
    Adds a sidebar section for filtering the dataframe.
    
    Args:
        df: The input DataFrame.
        
    Returns:
        pd.DataFrame: The filtered DataFrame.
    """
    st.sidebar.header("Filtros")
    df_filtered = df.copy()
    
    # Select columns to display
    all_columns = df.columns.tolist()
    selected_columns = st.sidebar.multiselect("Seleccionar Columnas a Mostrar", all_columns, default=all_columns)
    
    if selected_columns:
        df_filtered = df_filtered[selected_columns]
    
    # Numerical filters
    st.sidebar.subheader("Filtros Numéricos")
    numeric_columns = df.select_dtypes(include=['number']).columns.tolist()
    
    for col in numeric_columns:
        if col in df_filtered.columns:
            min_val = float(df[col].min())
            max_val = float(df[col].max())
            
            # Use slider only if there is a range
            if min_val < max_val:
                values = st.sidebar.slider(
                    f"Rango para {col}",
                    min_val, max_val, (min_val, max_val)
                )
                df_filtered = df_filtered[
                    (df_filtered[col] >= values[0]) & 
                    (df_filtered[col] <= values[1])
                ]
                
    return df_filtered
