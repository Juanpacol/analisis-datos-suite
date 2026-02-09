import pandas as pd
import streamlit as st

def load_data(file):
    """
    Loads data from a CSV or Excel file.
    
    Args:
        file: The uploaded file object.
        
    Returns:
        pd.DataFrame: The loaded pandas DataFrame, or None if error.
    """
    if file is None:
        return None
    
    try:
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        elif file.name.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file)
        else:
            st.error("Formato de archivo no soportado. Por favor sube un archivo CSV o Excel.")
            return None
        return df
    except Exception as e:
        st.error(f"Error al cargar el archivo: {e}")
        return None

def convert_df(df):
    """
    Converts DataFrame to CSV for download.
    
    Args:
        df: The pandas DataFrame.
        
    Returns:
        bytes: The CSV data encoded in utf-8.
    """
    return df.to_csv(index=False).encode('utf-8')
