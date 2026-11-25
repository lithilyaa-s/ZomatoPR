import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
from pathlib import Path

# ==========================================================
# Page Configuration
# ==========================================================

st.set_page_config(
    page_title="Zomato Restaurant Rating Predictor",
    page_icon="🍽️",
    layout="wide"
)
# ==========================================================
# Custom Theme
# ==========================================================

st.markdown("""
<style>

/* Main App */
.stApp{
    background-color:#0F1117;
}

/* Hide Streamlit Menu */
#MainMenu{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

header{
    visibility:hidden;
}

/* Main Title */

.main-title{
    font-size:46px;
    font-weight:700;
    color:white;
    margin-bottom:8px;
}

/* Subtitle */

.subtitle{
    color:#A0A6B3;
    font-size:18px;
    margin-bottom:35px;
}

/* Divider */

hr{
    border:1px solid #262730;
}

</style>
""", unsafe_allow_html=True)

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "zomato_rating_model.pkl"
DATA_PATH = BASE_DIR / "data" / "processed" / "zomato_processed.csv"

# ==========================================================
# Load Model
# ==========================================================

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    st.error(f"Unable to load model:\n{e}")
    st.stop()

# ==========================================================
# Load Dataset
# ==========================================================

try:
    df = pd.read_csv(DATA_PATH)
except Exception as e:
    st.error(f"Unable to load dataset:\n{e}")
    st.stop()

# ==========================================================
# Clean Dataset
# ==========================================================

df["Rating"] = df["Rating"].replace("Like", pd.NA)
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")

df["Cost"] = (
    df["Cost"]
    .astype(str)
    .str.replace(",", "", regex=False)
)

df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")

df = df.dropna(
    subset=[
        "Rating",
        "Review",
        "Restaurant",
        "Cost",
        "Cuisines"
    ]
)

# ==========================================================
# Title
# ==========================================================

st.markdown("""
<div class="main-title">
Zomato Restaurant Rating Predictor
</div>

<div class="subtitle">
Predict restaurant ratings using machine learning trained on thousands of customer reviews.
</div>
""", unsafe_allow_html=True)

st.divider()

# ==========================================================
# Sideba
# ==========================================================
# ==========================================================
# Prediction Panel
# ==========================================================

st.markdown("## Prediction")

left, right = st.columns(2)

with left:

    restaurant = st.selectbox(
        "Restaurant",
        sorted(df["Restaurant"].unique())
    )

    cuisine = st.selectbox(
        "Cuisine",
        sorted(df["Cuisines"].unique())
    )

with right:

    cost = st.number_input(
        "Average Cost (₹)",
        min_value=100,
        max_value=5000,
        value=500,
        step=50
    )

# ==========================================================
# Review Input
# ==========================================================

review = st.text_area(
    "Customer Review",
    height=180,
    placeholder="Write a detailed restaurant review..."
)

predict = st.button(
    "Predict Rating",
    width="stretch"
)

# ==========================================================
# Prediction
# ==========================================================

if predict:

    if review.strip() == "":
        st.warning("Please enter a review.")

    else:

        input_df = pd.DataFrame({
            "Review": [review],
            "Restaurant": [restaurant],
            "Cost": [cost],
            "Cuisines": [cuisine]
        })

        prediction = model.predict(input_df)

        st.success(
            f"⭐ Predicted Rating: {prediction[0]:.2f} / 5"
        )

# ==========================================================
# Dataset
# ==========================================================

with st.expander("📄 View Dataset"):

    st.dataframe(
        df.head(10),
        width="stretch"
    )

# ==========================================================
# Dashboard
# ==========================================================

st.divider()

st.subheader("📊 Dashboard")

total_restaurants = df["Restaurant"].nunique()
total_reviews = len(df)
average_rating = round(df["Rating"].mean(), 2)
average_cost = round(df["Cost"].mean())

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "🍴 Restaurants",
        total_restaurants
    )

with col2:
    st.metric(
        "📝 Reviews",
        total_reviews
    )

with col3:
    st.metric(
        "⭐ Average Rating",
        average_rating
    )

with col4:
    st.metric(
        "💰 Average Cost",
        f"₹{average_cost}"
    )

# ==========================================================
# Rating Distribution
# ==========================================================

st.divider()

st.subheader("⭐ Rating Distribution")

fig = px.histogram(
    df,
    x="Rating",
    nbins=10,
    title="Distribution of Ratings",
    color="Rating"
)

fig.update_layout(
    template="plotly_dark",
    height=500,
    showlegend=False
)

st.plotly_chart(
    fig,
    width="stretch"
)   
# ==========================================================
# Top 10 Restaurants
# ==========================================================

st.divider()

st.subheader("🏆 Top 10 Restaurants by Number of Reviews")

restaurant_counts = (
    df["Restaurant"]
    .value_counts()
    .head(10)
    .reset_index()
)

restaurant_counts.columns = ["Restaurant", "Reviews"]

fig_restaurants = px.bar(
    restaurant_counts,
    x="Restaurant",
    y="Reviews",
    color="Reviews",
    title="Top 10 Most Reviewed Restaurants"
)

fig_restaurants.update_layout(
    template="plotly_dark",
    height=500,
    xaxis_title="Restaurant",
    yaxis_title="Number of Reviews"
)

st.plotly_chart(fig_restaurants, width="stretch")

# ==========================================================
# Top 10 Cuisines
# ==========================================================

st.divider()

st.subheader("🍜 Top 10 Most Popular Cuisines")

cuisine_counts = (
    df["Cuisines"]
    .value_counts()
    .head(10)
    .reset_index()
)

cuisine_counts.columns = ["Cuisine", "Count"]

fig_cuisine = px.bar(
    cuisine_counts,
    x="Cuisine",
    y="Count",
    color="Count",
    title="Top 10 Cuisines"
)

fig_cuisine.update_layout(
    template="plotly_dark",
    height=500,
    xaxis_title="Cuisine",
    yaxis_title="Restaurants"
)

st.plotly_chart(fig_cuisine, width="stretch")