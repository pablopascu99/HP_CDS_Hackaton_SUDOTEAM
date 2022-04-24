import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium
from query import bicis_personas


def bicis():
    st.write(bicis_personas())