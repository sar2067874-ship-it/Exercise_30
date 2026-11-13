from pathlib import Path
import pandas as pd
import streamlit as st

st.title("Mammal Sleep, Lifespan, and Exposure")

csv_path = Path(__file__).with_name("mammals.csv")
mammals = pd.read_csv(csv_path)

species_options = mammals["species"].dropna().unique().tolist()

selected_species = st.multiselect(
    "Choose mammals to compare", 
    options=species_options,
    default=species_options[:5],)

if selected_species: 
        selected = mammals[mammals["species"].isin(selected_species)]
        st.subheader("Total Sleep")
        st.bar_chart(selected, x="species", y="total_sleep", horizontal =True)
        st.subheader("Life Span")
        st.bar_chart(selected, x="species", y="life_span", horizontal=True)
else: 
        st.info("Choose at least one species to see the charts.")

st.subheader("Exposure by Mammal")
st.bar_chart(selected, x="species", y="exposure")
one_species = st.selectbox("Choose a mammal", options=species_options)
species_data = mammals.loc[mammals["species"] == one_species, ["total_sleep", "exposure"]].dropna()
if species_data.empty:
    st.info(f"Sleep or exposire data is unavailable for {one_species}.")
else: 
    st.write(one_species)
    st.scatter_chart(species_data, x="exposure", y="total_sleep")




