import streamlit as st
import ModelAnalyzer as ma
import matplotlib.pyplot as plt

if "array_buffer" not in st.session_state:
    st.subheader("Please upload a ifc file in the Dashboard page")
else:
    model = st.session_state.ifc_model
    model_analyse = ma.ModelAnalyzer(model)
    product = model_analyse.count_products("IfcProduct")
    elements = model_analyse.count_products("IfcElement")
    Buildingelements = model_analyse.count_products("IfcBuildingElement")

    # st._chart(data=product["Quantity"],x=product["type"])
    st.title("IFC Diagnostic")
    st.subheader("Product Diagnostic")
    st.table(product)
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = product["type"]
    sizes = product["Quantity"]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1,True)

    st.subheader("Entity Diagnostic")
    Entity = model_analyse.count_products("IfcRoot")
    st.table(Entity)

    labels = Entity["type"]
    sizes = Entity["Quantity"]
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1, True)














