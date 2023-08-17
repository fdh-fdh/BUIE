import streamlit as st
import BreakdownExtractor as be
import streamlit_tree_select as sts


if "array_buffer" not in st.session_state:
    st.subheader("Please upload a ifc file in the Dashboard page")
else:
    model = st.session_state.ifc_model
    extractor = be.BreakdownExtractor(model)
    nodes = extractor.get_spatial_breakdown()
    return_select = sts.tree_select(nodes)
    st.write(return_select)


