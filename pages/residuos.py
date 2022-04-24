from cmath import nan
from pyparsing import And
import streamlit as st
from query import contenedores
import pandas as pd
import plotly.graph_objects as go
import numpy as np

def residuos():
    st.write("test")
    # contenedores()
    contenedores = pd.read_csv('output/densidad_cubos_censo.csv', sep=';')
    st.write(contenedores)
    x = contenedores["Distrito"].drop_duplicates()
    y = contenedores["Tipo"].drop_duplicates()
    st.write(x)
    df = pd.DataFrame(np.zeros((17, 5)), index=x.to_numpy(), columns=y.to_numpy())
    st.write(df)
    names = x
    i=0
    for n in x:
        for m in y:
            value =(contenedores.where(contenedores["Distrito"]==n).where(contenedores["Tipo"]==m)["Contenedores"].dropna())
            # print(value)
            if value.size != 0:
                st.write(n,m,type(n))
                st.write(value, type(value))

    #             st.write(n, m, "error")


    # fig = go.Figure()
    # fig.add_trace(go.Bar(x=names,
    #                 y=vidrio["Contenedores"],
    #                 name='Goles en casa',
    #                 marker_color='rgb(220,20,60)'
    #                 ))
    # fig.add_trace(go.Bar(x=names,
    #                 y=papel["Contenedores"],
    #                 name='Goles fuera',
    #                 marker_color='rgb(26, 118, 255)'
    #                 ))
    # fig.add_trace(go.Bar(x=names,
    #                 y=organico["Contenedores"],
    #                 name='Goles concedidos en casa',
    #                 marker_color='rgb(255,215,0)'
    #                 ))
    # # fig.add_trace(go.Bar(x=names,
    # #                 y=goalsConcededAway,
    # #                 name='Goles concedidos fuera',
    # #                 marker_color='rgb(34,139,34)'
    # #                 ))

    # fig.update_layout(
    #     title='Goles(en casa, fuera y concedidos) de los equipos top de La Liga',
    #     xaxis_tickfont_size=14,
    #     yaxis=dict(
    #         title='Goals',
    #         titlefont_size=16,
    #         tickfont_size=14,
    #     ),
    #     legend=dict(
    #         x=1,
    #         y=1.0,
    #         bgcolor='rgba(255, 255, 255, 0)',
    #         bordercolor='rgba(255, 255, 255, 0)'
    #     ),
    #     barmode='group',
    #     bargap=0.15, # gap between bars of adjacent location coordinates.
    #     bargroupgap=0.1 # gap between bars of the same location coordinate.
    # )
    # st.plotly_chart(fig)