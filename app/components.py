import streamlit as st

def hero():

    st.markdown(
        """
        <div class="hero-title">
        Zomato Restaurant Rating Predictor
        </div>

        <div class="hero-subtitle">
        Predict restaurant ratings using machine learning trained on thousands of customer reviews.
        </div>
        """,
        unsafe_allow_html=True
    )


def metric_card(title,value):

    st.markdown(
        f"""
        <div class="card">

        <div class="card-title">

        {title}

        </div>

        <div class="card-value">

        {value}

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def prediction_card(rating):

    st.markdown(
        f"""
        <div class="prediction">

        <div class="prediction-label">

        Prediction

        </div>

        <div class="prediction-value">

        {rating:.2f}

        </div>

        <div class="prediction-label">

        out of 5

        </div>

        </div>
        """,
        unsafe_allow_html=True
    )