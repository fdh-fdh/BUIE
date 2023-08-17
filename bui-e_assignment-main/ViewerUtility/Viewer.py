import streamlit as st

# inspired and tweaked based on:
# https://github.com/myoualid/ifc-101-course/tree/main/episode-09/streamlit-ifc-final/pages


# -- -- -- STREAMLIT IFC-JS COMPONENT MAGIC -- -- --
from pathlib import Path
from typing import Optional
import streamlit.components.v1 as components

# Tell streamlit that there is a component called ifc_js_viewer,
# and that the code to display that component is in the "frontend" folder
frontend_dir = (Path(__file__).parent / "frontend-viewer").absolute()
_component_func = components.declare_component(
    "ifc_js_viewer", path=str(frontend_dir))


# Create the python function that will be called
def run_ifc_js_viewer(url: Optional[str] = None):
    component_value = _component_func(url=url)
    return component_value

# -- -- -- STREAMLIT IFC-JS COMPONENT MAGIC -- -- --


def __draw_3d_viewer():
    def get_current_ifc_file():
        return st.session_state.array_buffer

    st.session_state.ifc_js_response = run_ifc_js_viewer(get_current_ifc_file())


def view_model():
    """
    call this function to visualize the IFC model
    :return:
    """
    st.header(":tv: IFC.js Viewer")
    if "ifc_model" in st.session_state and st.session_state["ifc_model"]:
        if "ifc_js_response" not in st.session_state:
            st.session_state["ifc_js_response"] = ""
        __draw_3d_viewer()

    else:
        st.warning("Please load a file first. ")


