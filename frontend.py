import streamlit as st

from pages.residuos import residuos
from pages.trafico import trafico
from pages.calidad import calidad
from pages.seguridad import seguridad
from pages.energias import energias
from pages.sostenibilidad import sostenibilidad

st.set_page_config(
    page_title="Sudo Team",
    page_icon="💻",
)

st.title("Fase final: Sudo Team")


sections = [
    "0. Introducción",
    "1. Residuos",
    "2. Tráfico",
    "3. Calidad de vida",
    "4. Seguridad civil",
    "5. Energías renovables",
    "6. Sostenibilidad",
]


with st.sidebar:
    add_radio = st.radio("Índice", sections)


if add_radio == "0. Introducción":
    st.write(
        """
     👋 En esta web encontrará información de utilidad para distintos futuros servicios que puede ofrecer un banco.

     🌅 Esta información esta basada en datos de movimientos bancarios y el tiempo atmosférico de la región de Almeria en el año 2015.

     👈 En la barra lateral podrá ir navegando por los distintos KPIs.

     🚀 Pulsando en el siguiente botón podrá actualizar las consultas Spark por si hay nuevos datos"""
    )

if add_radio == "1. Residuos":
    residuos()

if add_radio == "2. Tráfico":
    trafico()

if add_radio == "3. Calidad de vida":
    calidad()

if add_radio == "4. Seguridad civil":
    seguridad()

if add_radio == "5. Energías renovables":
    energias()

if add_radio == "6. Sostenibilidad":
    sostenibilidad()
