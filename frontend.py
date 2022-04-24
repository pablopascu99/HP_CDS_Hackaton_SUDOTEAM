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

hide_st_style = """
            <style>
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


# st.title("Fase final: Sudo Team")

st.sidebar.image: st.sidebar.image("sudo_team.png", use_column_width=True)

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
     👋 Bienvenido a nuestra propuesta de dashboard para la Final del CDS Challengue 2021/2022.

     🌅 Esta información esta basada en datos de movimientos ofrecidos por la organización.

     👈 En la barra lateral podrá ir navegando por los distintos KPIs.

     🚀 Espero que """
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
