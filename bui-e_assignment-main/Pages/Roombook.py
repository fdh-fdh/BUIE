import streamlit as st
import ModelAnalyzer as ma
import matplotlib.pyplot as plt


def find_the_level(psets, level:str):
    import math
    container ={"Category":[],"area":[],"Volume":[],"Height":[]}
    for i in psets:
        if i["PSet_Revit_Constraints"]["Level"] == level:
            name = i["PSet_Revit_Identity Data"]["Name"]
            try:
                container["Category"].index(name)
            except ValueError:
                container["Category"].append(i["PSet_Revit_Identity Data"]["Name"])
                container["area"].append(math.ceil(float(i["PSet_Revit_Dimensions"]["Area"])))
                container["Volume"].append(math.ceil(float(i["PSet_Revit_Dimensions"]["Volume"])))
                container["Height"].append(math.ceil(float(i["PSet_Revit_Dimensions"]["Unbounded Height"])))
            else:
                a = container["Category"].index(name)
                container["area"][a] += math.ceil(float(i["PSet_Revit_Dimensions"]["Area"]))

    return container


def find_room(psets, Room:str):
    import math
    container = {"Level": [], "area": [], "Volume": [], "Height": []}
    for i in psets:
        if i["PSet_Revit_Identity Data"]["Name"] == Room:
             Level = i["PSet_Revit_Constraints"]["Level"]
             try:
                container["Level"].index(Level)
             except ValueError:
                container["Level"].append(i["PSet_Revit_Constraints"]["Level"])
                container["area"].append(math.ceil(float(i["PSet_Revit_Dimensions"]["Area"])))
                container["Volume"].append(math.ceil(float(i["PSet_Revit_Dimensions"]["Volume"])))
                container["Height"].append(math.ceil(float(i["PSet_Revit_Dimensions"]["Unbounded Height"])))
             else:
                a = container["Level"].index(Level)
                container["area"][a] += math.ceil(float(i["PSet_Revit_Dimensions"]["Area"]))
    return container

def main():
    if "array_buffer" not in st.session_state:
        st.subheader("Please upload a ifc file in the Dashboard page")
    else:
        st.title("Roombook")
        model = st.session_state.ifc_model
        model_analyse = ma.ModelAnalyzer(model)
        pset,spaceinfo = model_analyse.get_space_data()

        tab1, tab2 = st.tabs(["Sort with Rooms","Sort with Level"])

        with tab1:
            st.header("Room")
            option = st.selectbox(
                "select level to visual space capability ", list(dict.fromkeys(spaceinfo["SpaceCategory"])))
            Roominfo = find_room(pset, option)
            if Roominfo == {}:
                st.write("room information not available")
            st.table(Roominfo)
            # # using matplotlab to visual pi chart
            # labels = Roominfo["Category"]
            #
            # fig1, axs = plt.subplots()
            # axs.pie(levelinfo["area"], labels=labels, autopct='%1.1f%%', shadow=True)
            #
            # st.pyplot(fig1, True)
        with tab2:
            st.header("Level")
            option = st.selectbox(
                "select level to visual space capability ",list(dict.fromkeys(spaceinfo["SpaceLevel"])))
            levelinfo = find_the_level(pset,option)
            if levelinfo == {}:
                st.write("room information not available")
            st.table(levelinfo)
            # using matplotlab to visual pi chart
            labels = levelinfo["Category"]

            fig1, axs= plt.subplots()
            axs.pie(levelinfo["area"], labels=labels, autopct='%1.1f%%', shadow=True)

            # Shift the second slice using explode
            # axs[0, 1].pie(levelinfo["Volume"], labels=labels, autopct='%.0f%%', shadow=True,
            #               )
            # axs[1, 0].pie(levelinfo["Height"], labels=labels, autopct='%.0f%%', shadow=True,
            #               )

            st.pyplot(fig1, True)



if __name__ == "__main__":
    # session_state is used to use variables across multiple pages and manipulate their values
    session = st.session_state

    # run the main function
    main()







