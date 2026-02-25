import streamlit as st
import pandas as pd

@st.cache_data
def load_main_data():

    file_id_all = st.secrets["FILE_ID_ALL"]
    file_id_credit = st.secrets["FILE_ID_CREDIT"]

    url_all = f"https://drive.google.com/uc?export=download&id={file_id_all}"
    url_credit = f"https://drive.google.com/uc?export=download&id={file_id_credit}"

    df_projects = pd.read_csv(url_all)
    df_credits = pd.read_csv(url_credit)

    return df_projects, df_credits
