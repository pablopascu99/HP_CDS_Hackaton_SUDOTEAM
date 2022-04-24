import streamlit as st
import pandas as pd
import json
from streamlit_folium import folium_static
import folium
import numpy as np


def seguridad():
    agree = st.checkbox("Justificación")

    if agree:
        name = "multasCount.csv"
        df = pd.read_csv(
            "output/{}".format(name), header="infer", sep=";", encoding="UTF-8"
        )
        st.write(df)

    name = "accidentesTipo.csv"
    df = pd.read_csv(
        "output/{}".format(name), header="infer", sep=";", encoding="UTF-8"
    )

    option = st.selectbox(
        "Qué tipo de accidente desea visualizar?",
        (
            "Colisión lateral",
            "Colisión fronto-lateral",
            "Atropello a animal",
            "Solo salida de la vía",
            "Atropello a persona",
            "Colisión múltiple",
            "Otro",
            "Caída",
            "Despeñamiento",
            "Vuelco",
        ),
    )

    df = df.where(df["tipo_accidente"] == option)

    with open("madrid_distritos.json") as f:
        madrid_distritos = json.load(f)

    m = folium.Map(location=[40.42, -3.70], zoom_start=10.45)
    folium.Choropleth(
        # topojson="objects.almeria_wm",
        geo_data=madrid_distritos,
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
