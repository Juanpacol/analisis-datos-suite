import streamlit as st

def set_page_config():
    """
    Sets the initial page configuration for Streamlit.
    """
    st.set_page_config(
        page_title="Data Extractor App",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def show_footer():
    """
    Displays a footer in the sidebar.
    """
    st.sidebar.markdown("---")
    st.sidebar.markdown(
        """
        <div style="text-align: center;">
            <p>Desarrollado con ❤️ usando Streamlit</p>
        </div>
        """,
        unsafe_allow_html=True
    )
