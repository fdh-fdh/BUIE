import streamlit as st
import ifcopenshell as ifc
import ModelAnalyzer as MA
import ViewerUtility.Viewer as V



def callback_upload():
    # save the loaded IFC model into the session state manager
    session["array_buffer"] = session["uploaded_file"].getvalue()
    session["ifc_model"] = ifc.file.from_string(session["array_buffer"].decode("utf-8"))
    session["is_file_loaded"] = True






def main():
    # Define some general settings
    st.set_page_config(
        layout="wide",
        page_title="IFC Dashboard",
        page_icon="chart_with_upwards_trend"
    )

    with st.sidebar:
        st.markdown(":copyright: TUM CMS 2023")

    # Define page title
    st.title("IFC Dashboard")

    # Add file upload control
    st.subheader(':wrench: Model Loader')
    st.file_uploader("Choose a file", type=['ifc'], key="uploaded_file", on_change=callback_upload)
    # "callback_upload" is a callback function that is triggered once a file has been selected
    if "ifc_model" not in st.session_state:
        st.write("Model viewer is ready as soon as upload is succeed")

    if "is_file_loaded" in session and session["is_file_loaded"]:
        # print some nice messages
        st.success("Project successfully loaded :white_check_mark:")
        st.write(":repeat: You can reload a new file")

        # access the IFC model content
        model = session["ifc_model"]
        name = model.by_type("IfcProject")
        names = []
        for n in name:
            names.append(n.Name)

        V.view_model()


        st.subheader("Project Information" + str(names))
        st.write("the schema of the Model is: " + str(model.schema))
        element = model.by_type("IfcElement")[0]
        st.write("there are "+ str(len(element)) +" of elements were readed")
        st.write("there are " + str(len(model.by_type("IfcWall"))) + " walls were readed ")
        st.subheader("IFC_Products")
        IFC_Product = model.by_type("IfcProduct")
        pname = []
        for p in IFC_Product:
            pname.append(p.Name)
        st.table(pname)
        model_analyse = MA.ModelAnalyzer(model)
        st.subheader("Choose the Objecttype")

        if model.schema == "IFC2X3":
            st.write("For IFC2X3 is this Function not available")

        else:
            option = st.selectbox(
                "select IFC-Entität ",
                ('IfcBeamType', 'IfcWallType', 'IfcDoorType', 'IfcWindowType', 'IfcFurnitureType')
            )
            ifcBuildingElementen = model_analyse.get_instances_by_type_name(option)
            ename = {"Name":[],"list":[]}
            for i in ifcBuildingElementen:
                ename["Name"].append(i.Name)
                ename["list"].append(i)

            st.table(ename)








        # -- INSERT YOUR CODE HERE --- 

    else:
        st.warning("Please load a model. ")



if __name__ == "__main__":
    # session_state is used to use variables across multiple pages and manipulate their values
    session = st.session_state

    # run the main function
    main()
