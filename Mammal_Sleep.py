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
        sleep_chart_data = selected.rename(columns={"total_sleep": "Sleep in Hours", "life_span": "Life Span in Years", "exposure": "Exposure to the Elements", 
                                                   "species": "Species"})
        
        st.subheader("Total Sleep")
        st.bar_chart(sleep_chart_data, x="Species", y="Sleep in Hours", horizontal =True)
    
        st.subheader("Life Span")
        st.bar_chart(sleep_chart_data, x="Species", y="Life Span in Years", horizontal=True)
    
        st.subheader("Exposure While Sleeping")
        st.markdown("1 = least exposed to the elements (most protected)")
        st.markdown("5 = most exposed to the elements (least protected)")
        st.bar_chart(sleep_chart_data, x="Species", y="Exposure to the Elements")
    
else: 
        st.info("Choose at least one species to see the charts.")







