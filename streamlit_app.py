# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col
import requests


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
my_dataframe = session.table("smoothies.public.fruit_options").select(col('fruit_name'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients : ',
    my_dataframe,
    max_selections=5
)

if ingredients_list:
    ingredients_string = ''

    for fruit_chosen in ingredients_list : 
        ingredients_string += fruit_chosen + ' '

    #st.write(ingredients_string)

    my_insert_stmt = """insert into smoothies.public.orders(ingredients, name_on_order) 
        values ('""" + ingredients_string +"""','""" + name_on_order + """')"""
    #st.write(my_insert_stmt)

    time_to_insert = st.button('Submit order')

    if time_to_insert:
        session.sql(my_insert_stmt).collect()
        strSuccess = "Your smoothie is ordered, " + name_on_order
        st.success(strSuccess, icon="✅")

smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response.json())
