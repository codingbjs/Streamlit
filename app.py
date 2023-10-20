import streamlit as st
import pandas as pd

view = [100, 150, 30]
view
st.write('# Youtube view')
st.write('## raw')
st.bar_chart(view)

s_view = pd.Series(view)
s_view

