from pathlib import Path
import pandas as pd
import streamlit as st

st.title("How much do mammals sleep?")

csv_path = Path(__file__).with_name("mammals.csv")
mammals = pd.read_csv(csv_path)

species_options = mammals["species"].dropna().unique().tolist()

selected_species = st.multiselect(
    "Choose mammals to compare", 
    options=species_options,
    default=species_options[:5],)

if selected_species: 
        selected = mammals[mammals["species"].isin(selected_species)]

        st.subheader("total sleep")
        st.bar_chart(selected, x="species", y="total_sleep", horizontal =True)

        st.subheader("Life Span")
        st.bar_chart(selected, x="species", y="life_span", horizontal=True)
else: 
        st.info("Choose at least one species to see the charts.")

