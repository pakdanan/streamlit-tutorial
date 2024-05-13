# SPDX-FileCopyrightText: 2023 Fabian Neumann (TU Berlin), 2023
#
# SPDX-License-Identifier: MIT

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Power Plants", layout="wide")

# st.balloons()

st.title("Power Plants in Europe")


@st.cache_data
def load_powerplants():
    # url = "https://raw.githubusercontent.com/PyPSA/powerplantmatching/master/powerplants.csv"
    # return pd.read_csv(url, index_col=0)
    return pd.read_csv("id-power-plants.csv", index_col=0)


df = load_powerplants()

with st.sidebar:
    st.title("Data Science for Energy System Modelling")

    st.markdown(":+1: This notebook introduces you to the `streamlit` library.")

    # tech = st.selectbox(
    #     "Select a technology",
    #     ppl.primary_fuel.unique(),
    # )


hover_data = ['name', 'primary_fuel', "capacity_mw", 'owner']

# df = ppl.query("primary_fuel == @tech")

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
        #        range_color=(1900, 2022),
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("Sorry, no power plants to display!")
