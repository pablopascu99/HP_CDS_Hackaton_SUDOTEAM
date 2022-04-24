import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
import json

def bicis():
    name = "dist_bicis.csv"
    df = pd.read_csv(
        "output/{}".format(name), header="infer", sep=";", encoding="UTF-8"
    )

    with open("madrid_distritos.json", encoding="UTF-8") as f:
        madrid_distritos = json.load(f)

    st.write('##### Densidad de bicis durante el año por distrito')

    m = folium.Map(location=[40.42, -3.70], zoom_start=10.45)
    folium.Choropleth(
        # topojson="objects.almeria_wm",
        geo_data=madrid_distritos,
        name="choropleth",
        data=df,
        columns=["DISTRITO", "QT_BICIS"],
        key_on="feature.properties.name",
        # fill_color="RdYlGn_r",
        fill_color="YlGn",
        fill_opacity=0.5,
        line_opacity=0.5,
        legend_name="Densidad de bicis",
    ).add_to(m)
    folium_static(m)

    name = "dist_peatones.csv"
    df = pd.read_csv(
        "output/{}".format(name), header="infer", sep=";", encoding="UTF-8"
    )

    with open("madrid_distritos.json", encoding="UTF-8") as f:
        madrid_distritos = json.load(f)

    st.write('##### Densidad de peatones durante el año por distrito')

    m = folium.Map(location=[40.42, -3.70], zoom_start=10.45)
    folium.Choropleth(
        # topojson="objects.almeria_wm",
        geo_data=madrid_distritos,
        name="choropleth",
        data=df,
        columns=["DISTRITO", "QT_PEATONES"],
        key_on="feature.properties.name",
        # fill_color="RdYlGn_r",
        fill_color="YlGn",
        fill_opacity=0.5,
        line_opacity=0.5,
        legend_name="Densidad de peatones",
    ).add_to(m)
    folium_static(m)
    