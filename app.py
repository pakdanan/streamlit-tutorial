# SPDX-FileCopyrightText: 2023 Fabian Neumann (TU Berlin), 2023
#
# SPDX-License-Identifier: MIT

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Power Plants", layout="wide")

# st.balloons()

st.title("Power Plants in Indonesia")


@st.cache_data
def load_powerplants():
    url = "https://global-power-plants.datasettes.com/global-power-plants/global-power-plants.csv"
    return pd.read_csv(url, index_col=0)


df = load_powerplants()

with st.sidebar:
    st.title("Data Science for Energy System Modelling")

    st.markdown(":+1: This notebook introduces you to the `streamlit` library.")


hover_data = ['name', 'primary_fuel', "capacity_mw", 'owner']


if not df.empty:
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        mapbox_style="carto-positron",
        color="primary_fuel",
        size="capacity_mw",
        zoom=2,
        height=700,
        hover_data=hover_data,
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Sorry, no power plants to display!")
