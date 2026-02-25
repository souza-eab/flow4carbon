import streamlit as st

# Importações internas
from modules.data_loader import load_data
from modules.maps import render_map
from modules.vintage import render_vintage
from modules.storytelling import render_storytelling

# --------------------------------------------------
# CONFIGURAÇÃO GLOBAL
# --------------------------------------------------
st.set_page_config(
    page_title="Carbon Projects Dashboard",
    layout="wide"
)

# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():

    st.title("Carbon Projects Dashboard")

    # Carrega dados
    df_all, df_credit = load_data()

    # Menu lateral
    page = st.sidebar.selectbox(
        "Select Section",
        ["Map", "Vintage Analysis", "Storytelling"]
    )

    if page == "Map":
        render_map(df_all)

    elif page == "Vintage Analysis":
        render_vintage(df_credit)

    elif page == "Storytelling":
        render_storytelling(df_all)


if __name__ == "__main__":
    main()
