import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import calendar as cal
import seaborn as sns
from dateutil.relativedelta import relativedelta
import time


if st.button("Run Simulation"):

    df = pd.DataFrame()
    df["Nothing"] = [1,2,3]

    def getdata(df):
        return df.to_csv(index=False).encode('utf-8')

    st.download_button('Download Simulation', data=getdata(df), file_name='Simulation.csv')

