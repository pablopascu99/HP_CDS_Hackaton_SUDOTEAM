import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium


def trafico():

    name = "Anthem_CTC_Taxi_ReservaParadas.csv"
    df = pd.read_csv("data/{}".format(name), header="infer", sep=";", encoding="UTF-8")

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
    folium_static(m)
