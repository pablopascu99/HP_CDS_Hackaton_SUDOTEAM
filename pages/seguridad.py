import streamlit as st
import pandas as pd
import json
from streamlit_folium import folium_static
import folium
import numpy as np


def seguridad():

    # name = "Alcance.csv"
    # name = "Colisión frontal.csv"
    # name = "Vuelco.csv"
    # name = "Atropello a animal.csv"
    name = "Despeñamiento.csv"
    df = pd.read_csv(
        "output/accidentes/{}".format(name), header="infer", sep=";", encoding="UTF-8"
    )
    st.write(df)

    with open("madrid_distritos.json") as f:
        madrid_distritos = json.load(f)
    m = folium.Map(location=[40.42, -3.70], zoom_start=10.45)
    folium.Choropleth(
        geo_data=madrid_distritos,
        # topojson="objects.almeria_wm",
        name="choropleth",
        data=df,
        columns=["cod_distrito", "Cantidad"],
        key_on="feature.properties.cartodb_id",
        fill_color="RdYlGn_r",
        fill_opacity=0.5,
        line_opacity=0.5,
        legend_name="otra",
    ).add_to(m)
    folium_static(m)
