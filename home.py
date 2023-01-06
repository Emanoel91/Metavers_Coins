# 📚 Libraries
import streamlit as st
from PIL import Image


# Title
st.set_page_config(page_title='Metaverse Coins', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('Ⓜetaverse Coins')

# Content
c1, c2 = st.columns(2)

#c1.image(Image.open('Images/logo.JPG'))

st.subheader('📃 Introduction')


st.write(
    """
111
    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
222
    """
)

st.subheader('📖 Guidance')
st.write(
    """
333
    """
)


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="📌")
   # c1.image(Image.open('Images/analyst2.JPG'))
with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")
    #c2.image(Image.open('Images/flipside.JPG'))
with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")
   # c3.image(Image.open('Images/metricsdao.JPG'))





