import mysql.connector
import streamlit as st
import pandas as pd

def save_to_mysql(df, table_name):
    try:
        # 1. Limpieza de NaNs: Convertimos NaN a None (NULL en SQL)
        # Esto soluciona el error 'Unknown column nan'
        df_clean = df.replace({pd.NA: None, float('nan'): None})
        
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MELIODAS9341",
            database="db_date"
        )
        cursor = conn.cursor()

        # Crear tabla si no existe
        columns = ", ".join([f"`{col}` TEXT" for col in df_clean.columns])
        cursor.execute(f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns})")

        # Preparar la consulta
        cols_names = "`, `".join(df_clean.columns)
        placeholders = ", ".join(["%s"] * len(df_clean.columns))
        sql = f"INSERT INTO `{table_name}` (`{cols_names}`) VALUES ({placeholders})"
        
        # 2. Insertar los datos usando el DataFrame limpio
        for i, row in df_clean.iterrows():
            # Convertimos la fila a una tupla, asegurando que los NaNs ahora sean None
            cursor.execute(sql, tuple(row))
            
        conn.commit()
        st.success(f"✅ ¡Datos guardados exitosamente!")
        
    except mysql.connector.Error as err:
        st.error(f"❌ Error al conectar a MySQL: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()