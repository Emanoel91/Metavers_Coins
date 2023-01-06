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
     if query1 == 'Transactions Overview':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5954ddc8-9cdf-47cc-b4cb-a67a0d05f75b/data/latest')
     elif query1 == 'Daily Transactions Data':
        return pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/28aad408-cba3-4560-9235-7a5026a5cd1b/data/latest')
     return None

transactions_overview = get_data('Transactions Overview')
Daily_Transactions_Data = get_data('Daily Transactions Data')
Status_of_Transactions = get_data('Status of Transactions')
Statistical_Data_Number_of_Transactions = get_data('Statistical Data: Number of Transactions')
Top_20_TX_Signers_Base_on_Transactions_Count = get_data('Top 20 TX Signers Base on Transactions Count')
Top_20_TX_Receivers_Base_on_Transactions_Count = get_data('Top 20 TX Receivers Base on Transactions Count')
Transaction_Fees = get_data('Transaction Fees')
Total_Average_Transactions_Fee = get_data('Total/Average Transactions Fee')
Top_20_TX_Signers_Based_on_Paid_Fees = get_data('Top 20 TX Signers Based on Paid Fees')
Statistical_Data_Daily_Transaction_Fees = get_data('Statistical Data: Daily Transaction Fees')
Classification_of_Blocks_Based_on_TX_Count = get_data('Classification of Blocks Based on TX Count')
Block_with_Maximum_Transaction_Count = get_data ('Block Maximum Transaction Count')
Distribution_of_Transactions_Between_Blocks = get_data('Distribution of Transactions Between Blocks')
Classification_of_Transactions_Based_on_TX_Signers = get_data('Classification of Transactions Based on TX Signers')
Number_of_New_Addresses = get_data('Number of New Addresses')
Transactions_Hitmap_Day_of_Week = get_data('Transactions Hitmap: Day of Week')
Total_Transactions_Count_Over_Days_of_Week = get_data('Total Transactions Count Over Days of Week')
Total_Transactions_Count_Over_Hours_of_Day = get_data('Total Transactions Count Over Hours of Day')
Monthly_Transactions_Count_of_Top_TX_Signers = get_data('Monthly Transactions Count of Top TX Signers')
Monthly_Transactions_Count_of_Top_TX_Receivers = get_data('Monthly Transactions Count of Top TX Receivers')
Monthly_Transaction_Fees_of_Top_TX_Signers = get_data('Monthly Transaction Fees of Top TX Signers')
Time_interval_between_the_first_and_last_transaction = get_data('Time interval between the first and last transaction')
Distribution_of_the_number_of_activity_days = get_data('Distribution of the number of activity days')
Max_Avg_Median_Min_Transaction_Fees = get_data('Max/Avg/Median/Min Transaction Fees')

subtab_overview, subtab_heatmap = st.tabs(['Overview', 'Heatmap'])
with subtab_overview:
     st.subheader('Overview')


with subtab_heatmap:
     st.subheader('Heatmap of Swaps')
