import pandas as pd
import streamlit as st  
import numpy as np

def fetch_data(species, total_sleep, life_span:
    data_frames = []
    for species in species_:
        data_frames.append(species_data)
    
    data = pd.concat(data_frames, axis=1, keys=tickers)
    data.columns = species
    return data


