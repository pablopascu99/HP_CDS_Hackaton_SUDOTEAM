import streamlit as st
from streamlit_folium import folium_static
import folium
import numpy as np
import pandas as pd
import json


def calidad():
    name = "zonasVerdeDistrito.csv"
    df = pd.read_csv("output/{}".format(name), header="infer", sep=";", encoding="UTF-8")

    with open("madrid_distritos.json", encoding="UTF-8") as f:
        madrid_distritos = json.load(f)
    st.write("Zonas verdes por distrito")

    m = folium.Map(location=[40.42, -3.70], zoom_start=10.45)
    folium.Choropleth(
        # topojson="objects.almeria_wm",
        geo_data=madrid_distritos,
        name="choropleth",
        data=df,
        columns=["DISTRITO", "sum(SUPERFICIE (ha))"],
        key_on="feature.properties.name",
        # fill_color="RdYlGn_r",
        fill_color="YlGn",
        fill_opacity=0.5,
        line_opacity=0.5,
        legend_name="Densidad de zonas verdes",
    ).add_to(m)
    folium_static(m)
