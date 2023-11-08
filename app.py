import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import calendar as cal
import seaborn as sns
from dateutil.relativedelta import relativedelta
import time

slid = st.slider("slide me", min_value=0, max_value=10)

if st.button("Run Simulation"):

    df = pd.DataFrame()
    df["Nothing"] = [1,2,3]

    st.markdown("Don't make me dissapear :(")

    def getdata(df):
        return df.to_csv(index=False).encode('utf-8')

    st.download_button('Download Simulation', data=getdata(df), file_name='Simulation.csv')

