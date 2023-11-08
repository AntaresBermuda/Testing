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
    
    st.download_button('Download Simulation', data=getdata(), file_name='Simulation.csv')

