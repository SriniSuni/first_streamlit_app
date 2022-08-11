import streamlit
streamlit.title ("My Parents New Healthy Diner👌👌👌")
streamlit.header("Breakfast Menu✍")
streamlit.text(" Oatmeal")
streamlit.text("salads🥗🥛")
streamlit.text("Bread and Milk🥛")

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +"kiwi")



fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
streamlit.write('The user entered ', fruit_choice)

# Normalize json data 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#display as a report
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()


my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

Add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding', Add_my_fruit)

insert into fruit_load_list values('from streamlit')
