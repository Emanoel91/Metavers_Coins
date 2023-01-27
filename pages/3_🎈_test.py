# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
from PIL import Image
	
theme_plotly = None # None or streamlit
	
# Structure
st.set_page_config(page_title='Price status - Metaverse Coins', page_icon=':chart_with_upwards_trend:', layout='wide')
st.title('💰 Price status')
	
# Cover
c1 , c2 = st.columns(2)
	
#c1.image(Image.open('Images/transactions.JPG'))
	
	
	
# dash_style
with open('style.css')as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
	
# flipside API
@st.cache(ttl=600)
def get_data(query1):
     if query1 == 'ALICE Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/4ccb8e8b-f402-45f1-b566-ffd4137b3f40/data/latest')
     elif query1 == 'AXS Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/a0bdfb0c-682b-4ce8-9dc4-0eca09ff67cc/data/latest')
     elif query1 == 'ENJ Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/52cfb301-f485-45a8-b530-150327c33a74/data/latest')
     elif query1 == 'MANA Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/41239f41-1c18-430c-98ff-ae270dc63733/data/latest')
     elif query1 == 'SAND Price':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/44390576-c37d-47ce-a965-e46ae0b7589d/data/latest')
     elif query1 == 'ALICE Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/50fdb41c-bd0f-40ed-aa99-7d26473f6a2f/data/latest')
     elif query1 == 'AXS Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/6cbdb3c4-ddac-4c58-b8c5-a9f663b06338/data/latest')
     elif query1 == 'ENJ Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/fcb52c3f-fe06-40da-8533-424085c7681b/data/latest')
     elif query1 == 'MANA Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/c6bc79d1-1cc2-4194-a7c5-54a7613dfe4f/data/latest')
     elif query1 == 'SAND Price Metric':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/23e7ef45-1c0c-47ad-9601-0704189452d4/data/latest')
     elif query1 == 'ALICE Price ATH':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/392bbd12-3ba3-4fa8-844b-6bf8f81405e5/data/latest')
     elif query1 == 'NORMAL DLY sample':
        return pd.read_json('')
     return None

ALICE_Price = get_data('ALICE Price')
AXS_Price = get_data('AXS Price')
ENJ_Price = get_data('ENJ Price')
MANA_Price = get_data('MANA Price')
SAND_Price = get_data('SAND Price')
ALICE_Price_Metric = get_data('ALICE Price Metric')
AXS_Price_Metric = get_data('AXS Price Metric')
ENJ_Price_Metric = get_data('ENJ Price Metric')
MANA_Price_Metric = get_data('MANA Price Metric')
SAND_Price_Metric = get_data('SAND Price Metric')
ALICE_Price_ATH = get_data('ALICE Price ATH')
NORMAL_DLY_sample = get_data('NORMAL DLY sample')

             
