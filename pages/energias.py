import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
import json


def paneles():

    st.write('##### Disposión de placas solares en Madrid')

    name = "Anthem_CTC_InstalacionesFotovoltaicas2.csv"
    df = pd.read_csv("output/{}".format(name), header="infer", sep=";", encoding = 'ISO-8859-1')

    m = folium.Map(location=[40.42, -3.70], zoom_start=11)

    for i in range(0, len(df)):
        folium.Marker(
            location=[df.iloc[i]["Latitud"], df.iloc[i]["Longitud"]],
            icon=folium.DivIcon(
                html=f"""
            <div><img src="https://pngimg.com/uploads/solar_panel/small/solar_panel_PNG106.png" width="25" height="25">
                </div>"""
            ),
        ).add_to(m)

    with open("madrid_distritos.json", encoding="UTF-8") as f:
        madrid_distritos = json.load(f)

    folium.Choropleth(
        # topojson="objects.almeria_wm",
        geo_data=madrid_distritos,
        name="choropleth",
        # data=df,
        # columns=["DISTRITO", "QT_BICIS"],
        # key_on="features.properties.BARRIO_MT",
        # fill_color="RdYlGn_r",
        fill_color="YlGn",
        fill_opacity=0.1,
        line_opacity=0.9,
        # legend_name="Densidad de bicis",
    ).add_to(m)
    folium_static(m)
