import streamlit as st
import pandas as pd
import pydeck as pdk
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Active Satellites Data Visualization (2016)", page_icon="🌍", layout="wide")

# Title
st.title("Satellites Global Analytics")

@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/f-masato-tanaka/active-satellites-data-visualization/refs/heads/main/main/database.csv'
    df = pd.read_csv(url)
    
    rename_columns = {
        'Official Name of Satellite': 'sat_name',
        'Country/Organization of UN Registry': 'country',
        'Purpose': 'purpose',
        'Detailed Purpose' : 'detailed_purpose',
        'Class of Orbit': 'orbit_class',
        'Date of Launch' : 'date_launch',
        'Expected Lifetime (Years)' : 'exp_life_years',
        'Launch Site' : 'launch_site',
    }
    df = df[list(rename_columns.keys())].rename(columns=rename_columns)
    
    acronym_map = {
        'USA': 'United States',
        'UK': 'United Kingdom',
        'South Korea': 'South Korea',
        'NR' : 'Unknown'
    }
    df['country'] = df['country'].replace(acronym_map)
    df.fillna('Unknown', inplace=True)
    return df

# Geolocation of the main Launch Sites
launch_site_coords = {
    'Kourou': [5.23, -52.76],
    'Baikonur Cosmodrome': [45.96, 63.30],
    'Cape Canaveral': [28.47, -80.57],
    'Kennedy Space Center': [28.57, -80.64],
    'Jiuquan Satellite Launch Center': [40.96, 100.28],
    'Tanegashima Space Center': [30.40, 130.97],
    'Satish Dhawan Space Centre': [13.71, 80.23],
    'Vandenberg AFB': [34.74, -120.57],
    'Xichang Satellite Launch Center': [28.24, 102.02],
    'Plesetsk Cosmodrome': [62.92, 40.57],
    'Taiyuan Satellite Launch Center': [38.84, 111.60],
    'Dombarovsky Air Base': [51.15, 59.84],
    'Wallops Island Flight Facility': [37.83, -75.48],
    'Uchinoura Space Center': [31.25, 131.07],
    'Semnan': [35.23, 53.92],
    'Kwajalein Atoll': [9.04, 167.64],
    'Sea Launch (Pacific Ocean)': [0.0, -154.0]
}

df = load_data()

# --- SIDEBAR ---
st.sidebar.header("Control Panel")

viz_type = st.sidebar.radio("Visualization type:", ("Density Map (Country)"))

st.sidebar.divider()

# Filters
all_purposes = sorted(df['purpose'].unique().astype(str))
selected_purpose = st.sidebar.multiselect("Select Purpose", all_purposes)

all_orbits = sorted(df['orbit_class'].unique().astype(str))
selected_orbit = st.sidebar.multiselect("Select Orbit Type", all_orbits)

all_launch_sites = sorted(df['launch_site'].unique().astype(str))
selected_launch_site = st.sidebar.multiselect("Select Launch Site", all_launch_sites)

# Logic for independent filters (OR logic as requested)
if not selected_purpose and not selected_orbit and not selected_launch_site:
    df_filtered = df.copy()
else:
    df_filtered = df[
        (df['purpose'].isin(selected_purpose)) | 
        (df['orbit_class'].isin(selected_orbit)) |
        (df['launch_site'].isin(selected_launch_site))
    ]

# --- RENDER MAPS ---

if viz_type == "Density Map (Country)":
    st.subheader("Dominance by Country")
    df_counts = df_filtered['country'].value_counts().reset_index()
    df_counts.columns = ['country', 'Quantity of Satellites']

    fig = px.choropleth(
        df_counts, 
        locations="country", 
        locationmode='country names',
        color="Quantity of Satellites", 
        hover_name="country",
        color_continuous_scale="Inferno"
    )
    fig.update_layout(height=800, margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("Select a visualization type from the sidebar.")

# Detailed Table
st.divider()
st.subheader("📝 Data Details")
st.dataframe(df_filtered[['sat_name', 'country', 'purpose', 'date_launch', 'orbit_class', 'launch_site', 'exp_life_years']], use_container_width=True)