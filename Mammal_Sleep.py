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
        sleep_chart_data = selected.rename(columns={"total_sleep": "Sleep in Hours", "life_span": "Life Span in Years", "exposure": "Exposure to the Elements". 
                                                   "species": "Species" })
        
        st.subheader("Total Sleep")
        st.bar_chart(selected, x="species", y="total_sleep", horizontal =True)
    
        st.subheader("Life Span")
        st.bar_chart(selected, x="species", y="life_span", horizontal=True)
    
        st.subheader("Exposure by Mammal")
        st.bar_chart(selected, x="species", y="exposure")
    
else: 
        st.info("Choose at least one species to see the charts.")







