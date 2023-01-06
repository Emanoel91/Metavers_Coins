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
     return None

ALICE_Price = get_data('ALICE Price')
AXS_Price = get_data('AXS Price')
ENJ_Price = get_data('ENJ Price')
MANA_Price = get_data('MANA Price')
SAND_Price = get_data('SAND Price')

subtab_ALICE, subtab_AXS, subtab_ENJ, subtab_MANA, subtab_SAND = st.tabs(['ALICE', 'AXS', 'ENJ', 'MANA','SAND'])
with subtab_ALICE:
     df = ALICE_Price
     fig = px.bar(df, x='DATE', y='RoPC', title='Range of Price Changes(RoPC)', log_y=False)
     fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=$USD)
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
#--------------------------------------------------------------------------------------------------------------------------
with subtab_AXS:
     df = AXS_Price
     fig = px.bar(df, x='DATE', y='RoPC', title='Range of Price Changes(RoPC)', log_y=False)
     fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=$USD)
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# -------------------------------------------------------------------------------------------------------------------------	
with subtab_ENJ:
     df = ENJ_Price
     fig = px.bar(df, x='DATE', y='RoPC', title='Range of Price Changes(RoPC)', log_y=False)
     fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=$USD)
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# --------------------------------------------------------------------------------------------------------------------------
with subtab_MANA:
     df = MANA_Price
     fig = px.bar(df, x='DATE', y='RoPC', title='Range of Price Changes(RoPC)', log_y=False)
     fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=$USD)
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
# --------------------------------------------------------------------------------------------------------------------------
with subtab_SAND:
     df = SAND_Price
     fig = px.bar(df, x='DATE', y='RoPC', title='Range of Price Changes(RoPC)', log_y=False)
     fig.update_layout(showlegend=False, xaxis_title=None, yaxis_title=$USD)
     st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
