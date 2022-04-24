from cmath import nan
from pyparsing import And
import streamlit as st
from query import contenedores
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def residuos():
    contenedores = pd.read_csv('output/densidad_cubos_censo.csv', sep=';')
    # st.write(contenedores)
    x = contenedores["Distrito"].drop_duplicates()
    y = contenedores["Tipo"].drop_duplicates()
    df = pd.DataFrame(np.zeros((17, 5)), index=x.to_numpy(), columns=y.to_numpy())
    for n in x:
        for m in y:
            value =(contenedores.where(contenedores["Distrito"]==n).where(contenedores["Tipo"]==m)["Contenedores"].dropna())
            if value.size != 0:
                df[m][n]=value.values[0]
    # st.write(df)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=x,
                    y=df["VIDRIO"],
                    name='Vidrio',
                    marker_color='green'
                    ))
    fig.add_trace(go.Bar(x=x,
                    y=df["PAPEL-CARTON"],
                    name='Papel',
                    marker_color='blue'
                    ))
    fig.add_trace(go.Bar(x=x,
                    y=df['RESTO'],
                    name='Resto',
                    marker_color='grey'
                    ))
    fig.add_trace(go.Bar(x=x,
                    y=df['ORGANICA'],
                    name='Orgánica',
                    marker_color='orange'
                    ))

    fig.add_trace(go.Bar(x=x,
                    y=df['ENVASES'],
                    name='Envases',
                    marker_color='yellow'
                    ))

    fig.update_layout(
        title='Gráfico por distritos de tipos contenedores por densidad de población',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Censo/Contenedores',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=1,
            y=1.0,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
    )
    st.plotly_chart(fig)
