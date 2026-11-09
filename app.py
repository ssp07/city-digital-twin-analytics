import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="City Digital Twin Analytics",
    page_icon="🌆",
    layout="wide"
)

# -------------------------
# Load Data
# -------------------------

traffic = pd.read_csv("traffic.csv")
weather = pd.read_csv("weather.csv")
air = pd.read_csv("air_quality.csv")
population = pd.read_csv("population.csv")

# -------------------------
# Merge Datasets
# -------------------------

city = traffic.merge(weather, on="zone")
city = city.merge(air, on="zone")
city = city.merge(population, on="zone")

# -------------------------
# Title
# -------------------------

st.title("🌆 City Digital Twin Analytics")

st.markdown("""
A Digital Twin of a Smart City integrating:

✅ Traffic Data

✅ Weather Data

✅ Air Quality Data

✅ Population Data

for urban intelligence and decision making.
""")

st.divider()

# -------------------------
# KPIs
# -------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Population",
    f"{city['population'].sum():,}"
)

col2.metric(
    "Avg AQI",
    f"{city['AQI'].mean():.0f}"
)

col3.metric(
    "Avg Temperature",
    f"{city['temperature'].mean():.1f}°C"
)

col4.metric(
    "Total Traffic",
    f"{city['traffic_volume'].sum():,}"
)

st.divider()

# -------------------------
# Traffic Dashboard
# -------------------------

st.subheader("🚗 Traffic by Zone")

fig1 = px.bar(
    city,
    x="zone",
    y="traffic_volume",
    color="traffic_volume",
    text="traffic_volume"
)

st.plotly_chart(fig1, use_container_width=True)

# -------------------------
# AQI Dashboard
# -------------------------

st.subheader("🏭 Air Quality Index")

fig2 = px.bar(
    city,
    x="zone",
    y="AQI",
    color="AQI",
    text="AQI"
)

st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Population Dashboard
# -------------------------

st.subheader("👨‍👩‍👧 Population Distribution")

fig3 = px.pie(
    city,
    values="population",
    names="zone"
)

st.plotly_chart(fig3, use_container_width=True)

# -------------------------
# Correlation Analysis
# -------------------------

st.subheader("📈 Traffic vs AQI")

fig4 = px.scatter(
    city,
    x="traffic_volume",
    y="AQI",
    size="population",
    color="zone",
    hover_name="zone"
)

st.plotly_chart(fig4, use_container_width=True)

# -------------------------
# Urban Intelligence Insights
# -------------------------

st.subheader("🧠 Urban Intelligence")

highest_traffic = city.loc[
    city["traffic_volume"].idxmax()
]

highest_pollution = city.loc[
    city["AQI"].idxmax()
]

highest_population = city.loc[
    city["population"].idxmax()
]

st.success(
    f"Highest traffic congestion: {highest_traffic['zone']} "
    f"({highest_traffic['traffic_volume']})"
)

st.warning(
    f"Highest pollution: {highest_pollution['zone']} "
    f"(AQI {highest_pollution['AQI']})"
)

st.info(
    f"Largest population: {highest_population['zone']} "
    f"({highest_population['population']:,})"
)

# -------------------------
# Data Explorer
# -------------------------

st.subheader("🔍 City Dataset")

st.dataframe(city, use_container_width=True)