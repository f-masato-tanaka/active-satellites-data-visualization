import streamlit as st
import pandas as pd

# 1. Page Configuration 
st.set_page_config(
    page_title="Active Satellites Data Visualization (2016)",
    page_icon="🛰️",
    layout="wide"
)

# 2. Subsection 
st.title("🛰️ Active Satellites Data Visualization (2016)")
st.subheader("Global Mapping and Analysis of Active Satellites (2016)")

st.markdown("---")

# 3. Introduction
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### Project Overview
    This interactive application provides a visual and statistical analysis of the active satellite orbiting Earth, from 2016 data.
    
    **Key Objectives:**
    * 🌍 **Geospatial Mapping:** Visualize satellite density by country of origin.
    * 🚀 **Launch Insights:** Analyze the primary launch sites.
    * 📡 **Technical Specs:** Filter data by orbit class (LEO, MEO, GEO) and satellite purpose.
    """)

# 4. References
with col2:
    st.info("""
    **Dataset Information**
    - **Reference:** [Kaggle Dataset](https://www.kaggle.com/datasets/ucsusa/active-satellites)
    """)

# 5. Future Improvements
st.markdown("""
    ### Future Improvements
    - **Most recent data:** Update the dataset to include the latest satellite launches and decommissions.
    - **More filters:** Add search filters.
    - **Update telecom-churn-ml to streamlit.**
    """)

st.markdown("---")

# 6. Credits
st.markdown("""
    ### Credits
    - **Dataset Source:** [Kaggle Dataset](https://www.kaggle.com/datasets/ucsusa/active-satellites)
    - **Developed by:** Fernando Masato Tanaka (https://github.com/f-masato-tanaka)
    """)


st.sidebar.success("Select a visualization mode above.")
st.markdown("---")