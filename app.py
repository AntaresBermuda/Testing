import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import calendar as cal
import seaborn as sns
from dateutil.relativedelta import relativedelta
import time


@st.cache(show_spinner=False)
def generate_download_link():
    # Code to generate the file you want to download
    # This function will only be executed once, and the output will be cached

    # Replace the following code with your own logic to generate the file
    file_contents = "Hello, this is the file content!"

    return file_contents

def main():
    # Generate the download link
    file_contents = generate_download_link()

    # Create a download button using st.download_button
    if st.button("Download File"):
        # When the button is clicked, download the file
        # You can specify the file name and content type
        st.download_button(
            label="Click here to download",
            data=file_contents,
            file_name="file.txt",
            mime="text/plain"
        )

if __name__ == "__main__":
    main()



#slid = st.slider("slide me", min_value=0, max_value=10)

#if st.button("Run Simulation"):

#    df = pd.DataFrame()
#    df["Nothing"] = [1,2,3]

#    st.markdown("Don't make me dissapear :(")

#    def getdata(df):
#        return df.to_csv(index=False).encode('utf-8')

#    if st.download_button('Download Simulation', data=getdata(df), file_name='Simulation.csv'):
#        st.markdown("????")