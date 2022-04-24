import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium


def paneles():
    name = "Anthem_CTC_InstalacionesFotovoltaicas2.csv"
    df = pd.read_csv("output/{}".format(name), header="infer", sep=";", encoding="UTF-8")
    # st.write(df)

    m = folium.Map(location=[40.42, -3.70], zoom_start=11)

    for i in range(0, len(df)):
        folium.Marker(
            location=[df.iloc[i]["Latitud"], df.iloc[i]["Longitud"]],
            icon=folium.DivIcon(
                html=f"""
            <div><img src="https://pngimg.com/uploads/solar_panel/small/solar_panel_PNG106.png" width=50vw height=50vw>
                </div>"""
            ),
        ).add_to(m)
    folium_static(m)
