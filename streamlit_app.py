# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

helpful_links = [
    "https://docs.streamlit.io",
    "https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit",
    "https://github.com/Snowflake-Labs/snowflake-demo-streamlit",
    "https://docs.snowflake.com/en/release-notes/streamlit-in-snowflake"
]

# Write directly to the app
st.title("My parents new healthy diner")
st.header("Breakfast Menu")
st.write("Omega 3 & Blueberry oatmeal")
st.write("Kale, spinach & rocket smoothie")
st.write("Hard-boiled free-range egg")

name_on_order = st.text_input('Name on Smoothie')
st.write('The name on your smoothie will be :', name_on_order)


cnx = st.connection("snowflake")
session = cnx.session()
my_dataframe = session.table("INTERNATIONAL_CURRENCIES.public.fruit_options").select(col('CURRENCIES'))