from pathlib import Path
import geopandas as gpd
import streamlit as st

KML_DIR = Path("kml")

@st.cache_data
def load_kml_by_project(project_id):

    for file in KML_DIR.glob(f"{project_id}_*.kml"):
        gdf = gpd.read_file(file, driver="KML")
        return gdf

    return None
