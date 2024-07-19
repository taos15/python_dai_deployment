import streamlit as st

from views.st_inputs import stream_slicer


def main_view():
    st.markdown("# Mushroom app")
    stream_slicer(
        "Test slicer",
    )


if __name__ == "__main__":
    main_view()
