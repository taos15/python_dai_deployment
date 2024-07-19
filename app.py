"""Streamlit app file"""

import streamlit as st
import pandas as pd
from src.mushroom_model import predict_mushroom
from views.main_page import main_view

observation = {
    "cap-diameter": [50],
    "stem-height": [20],
    "stem-width": [30],
    "has-ring": ["t"],
    "cap-shape": ["c"],
}

single_obs_df = pd.DataFrame(observation)

if __name__ == "__main__":
    current_prediction = predict_mushroom(single_obs_df)[0]

    print(f"model result: {current_prediction}")
    print(observation)

    main_view()

    if current_prediction == 0:
        st.markdown("### Mushroom not is poisonous.")
    else:
        st.markdown("### Mushroom is poiusonous")
