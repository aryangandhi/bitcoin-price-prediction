import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date

# Set the title of the Streamlit app
st.title("Bitcoin Price Prediction App")

# Allow users to select the start and end date through a calendar view
start_date = st.date_input("Start date", value=date(2023, 1, 1), min_value=date(2010, 1, 1))
end_date = st.date_input("End date", value=date(2024, 5, 1), min_value=start_date)

# Fetch Bitcoin prices in CAD based on the selected date range
ticker = yf.Ticker("BTC-CAD")
bitcoin_df = pd.DataFrame(ticker.history(start=start_date, end=end_date)['Close'])

# Display the data as a line chart
st.write("## Historical Bitcoin Prices (BTC-CAD)")

# Plot the data
fig, ax = plt.subplots()
ax.plot(bitcoin_df.index, bitcoin_df['Close'])
ax.set_xlabel("Date")
ax.set_ylabel("Close Price (CAD)")
ax.set_title("Historical Bitcoin Prices (BTC-CAD)")

# Calculate the number of days in the selected date range
num_days = (end_date - start_date).days

# Adjust the x-axis labels based on the number of days in the selected date range
if num_days <= 31:
    # For a range of one month or less, show day labels
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
elif num_days <= 365:
    # For a range of one year or less, show month labels
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
else:
    # For a range of more than one year, show quarter labels
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))

# Rotate date labels to avoid overlap
fig.autofmt_xdate()

# Set the font size for the x-axis labels
ax.tick_params(axis='x', labelsize=10)

# Display the plot in Streamlit
st.pyplot(fig)
