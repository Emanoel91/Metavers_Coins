# π Libraries
import streamlit as st
from PIL import Image


# Title
st.set_page_config(page_title='Metaverse Coins', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('βetaverse Coins')

# Content
c1, c2 = st.columns(2)

c1.image(Image.open('Images/logo.JPG'))

st.subheader('π Introduction')


st.write(
    """
111
    """
)

st.subheader('π― Purposes of Dashboard')
st.write(
    """
222
    """
)

st.subheader('π Guidance')
st.write(
    """
333
    """
)


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="π")
   # c1.image(Image.open('Images/analyst2.JPG'))
with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="π")
    #c2.image(Image.open('Images/flipside.JPG'))
with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="π‘")
   # c3.image(Image.open('Images/metricsdao.JPG'))





