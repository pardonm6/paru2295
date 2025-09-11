import streamlit as st
import numpy as np

st.set_page_config(
    page_title= "Pardy's Dashboard",
    page_icon=":bar_chart:",
)

# Sidebar configuration
st.sidebar.image("./assets/Screen Shot 2025-09-11 at 18.35.51 PM.png",)
tab = st.sidebar.radio(
    "Navigate",
    ["Home", "Project", "Data"]
)
st.sidebar.success("Select a tab above.")

# # Page information

# Main content based on selected tab
if tab == "Home":
    st.write("# Welcome to Pardy's Dashboard! 👋")
    st.write("## Aims:")
    st.markdown("""
        This dashboard was developed by Pardon to showcase various data visualizations and analyses.
        It is aimed to provide a proving ground for Github push abd pull skills.
    """)


elif tab == "Project":
    st.write("## Project")
    st.markdown("""
        The project aims at developing a machine learning model to predict the likelihood of Stroke.
        The domain area is Health and the project uses a dataset from Kaggle containing various lifestyle and health metrics.
    """)

elif tab == "Data":
    import streamlit as st
    import pandas as pd
    import numpy as np
    import plotly.express as px

    @st.cache_data
    def get_data():
        df = pd.DataFrame(
            np.random.randn(50, 20), columns=("col %d" % i for i in range(20))
        )
        return df

    @st.cache_data
    def convert_for_download(df):
        return df.to_csv().encode("utf-8")

    df = get_data()
    csv = convert_for_download(df)

    st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv",
    icon=":material/download:",
    )
    
    
    @st.cache_data
    def get_data():
        df = pd.DataFrame(
            np.random.randn(50, 2), columns=["Age", "Stroke risk"]
        )
        return df

    df = get_data()

    st.write("## Interactive Plot")
    fig = px.scatter(df, x="Age", y="Stroke risk", title="Stroke Risk Scatter Plot")
    st.plotly_chart(fig, use_container_width=True)

    st.write("## Aquired Data")
    st.dataframe(df)

    add_slider = st.slider(
        'Select a range of values',
        0.0, 100.0, (25.0, 75.0)
    )