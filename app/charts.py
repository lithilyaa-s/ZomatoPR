import plotly.express as px
import streamlit as st


def rating_distribution(df):

    fig = px.histogram(
        df,
        x="Rating",
        nbins=10,
        color="Rating"
    )

    fig.update_layout(

        template="plotly_dark",

        paper_bgcolor="#0F1117",

        plot_bgcolor="#161B22",

        font_color="white",

        showlegend=False,

        margin=dict(
            l=20,
            r=20,
            t=40,
            b=20
        ),

        height=420
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )