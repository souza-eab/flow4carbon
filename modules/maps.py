import streamlit as st
import folium
from streamlit_folium import st_folium
from modules.kml_loader import load_kml_by_project

def render_map_section(df_projects):

    st.header("Project Map")

    selected_project = st.selectbox(
        "Select Project",
        df_projects["project_id"].unique()
    )

    gdf = load_kml_by_project(selected_project)

    m = folium.Map(location=[-3, -60], zoom_start=4)

    if gdf is not None:
        folium.GeoJson(gdf).add_to(m)

    st_folium(m, width=1200)
