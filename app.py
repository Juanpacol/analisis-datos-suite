import streamlit as st
from filters import filter_dataframe
from visualizations import plot_data
from helpers import set_page_config, show_footer
from db_handler_mysql import save_to_mysql
from file_handler import load_data, convert_df 
from data_explorer import show_data_preview, show_data_info, show_statistics
from streamlit.components.v1 import html
def main():
    # 1. Configuración de la página
    set_page_config()
    
    st.title("📊 Data Extractor App")
    st.markdown("""
    Bienvenido a **Data Extractor App**. Esta aplicación te permite subir tus datasets (CSV o Excel),
    explorarlos, filtrarlos y visualizarlos de manera interactiva.
    """)
    
    # 2. Carga de Archivos
    st.sidebar.header("Cargar Datos")
    uploaded_file = st.sidebar.file_uploader("Sube tu archivo (CSV o Excel)", type=['csv', 'xlsx', 'xls'])
    
    if uploaded_file is not None:
        # Cargar datos
        df = load_data(uploaded_file)
        
        if df is not None:
            # 3. Filtrado de Datos
            df_filtered = filter_dataframe(df)
            
            # Tab layout for organization
            tab1, tab2, tab3 = st.tabs(["📋 Datos", "📈 Visualización", "ℹ️ Información"])
            
            with tab1:
                # 4. Exploración de Datos
                show_data_preview(df_filtered)
    
                # Botón para guardar en DB
                if st.button("🗄️ Guardar datos filtrados en Base de Datos"):
                    save_to_mysql(df_filtered, "datos_extraidos")
                
                # Descarga de datos filtrados
                csv = convert_df(df_filtered)
                st.download_button(
                    label="📥 Descargar CSV Filtrado",
                    data=csv,
                    file_name='dataset_filtrado.csv',
                    mime='text/csv',
                )
                
                
                
            with tab2:
                # 5. Visualizaciones
                plot_data(df_filtered)
                
            with tab3:
                # Estadísticas
                show_data_info(df_filtered)
                show_statistics(df_filtered)
            
                
        
    else:
        st.info("Por favor, sube un archivo desde el panel lateral para comenzar.")
        
        # Example Usage Instructions when no file is uploaded
        st.markdown("### ¿Cómo usar esta app?")
        st.markdown("""
        1. **Sube un archivo:** Usa el panel lateral para cargar un archivo `.csv` o `.xlsx`.
        2. **Filtra:** Selecciona las columnas que quieres ver y filtra por rangos numéricos.
        3. **Explora:** Revisa la vista previa de datos y las estadísticas en la pestaña 'Datos' e 'Información'.
        4. **Visualiza:** Ve a la pestaña 'Visualización' para ver histogramas y gráficos de barras interactivos.
        5. **Exporta:** Descarga los datos filtrados con un solo clic.
        """)

    # Footer
    show_footer()

if __name__ == "__main__":
    main()
