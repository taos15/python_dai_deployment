import streamlit as st


def stream_slicer(
    label: str, default_value=None, minValue=0.0, maxValue=100.0, **kargs
):
    """Slicer"""

    slicer_values = (
        st.slider(
            label,
            minValue,
            maxValue,
            ((minValue + maxValue) / 2 if not default_value else default_value),
            **kargs
        ),
    )
    st.write("Values:", slicer_values)
