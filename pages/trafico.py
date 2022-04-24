import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
import json
import numpy as np
from query import accidenteletal


def trafico():


    name = "Anthem_CTC_Taxi_ReservaParadas.csv"
    df = pd.read_csv("output/{}".format(name), header="infer", sep=";", encoding="UTF-8")

    m = folium.Map(location=[40.42, -3.70], zoom_start=11)

    for i in range(0, len(df)):
        folium.Marker(
            location=[df.iloc[i]["Latitud"], df.iloc[i]["Longitud"]],
            icon=folium.DivIcon(
                html=f"""
            <div><img src="https://www.pngrepo.com/png/48299/512/taxi.png" width="25" height="25">
                </div>"""
            ),
        ).add_to(m)

    # with open("madrid_barrios2.json", encoding="UTF-8") as f:
    #     madrid_barrios = json.load(f)

    with open("madrid_distritos.json", encoding="UTF-8") as f:
        madrid_distritos = json.load(f)
    # st.write()

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

    name2 = "letalidad_fecha.csv"
    df2 = pd.read_csv("output/{}".format(name2), header="infer", sep=";", encoding="UTF-8")

    st.write(df2)
    df2 = df2.set_index('fecha')
    chart_data = df2
    st.line_chart(chart_data)

