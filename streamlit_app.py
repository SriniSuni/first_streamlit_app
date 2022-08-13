import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title ("My Parents New Healthy Diner👌👌👌")
streamlit.header("Breakfast Menu✍")
streamlit.text(" Oatmeal")
streamlit.text("salads🥗🥛")
streamlit.text("Bread and Milk🥛")

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

my_fruit_list = my_fruit_list.set_index('Fruit')
# streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +"kiwi")



fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')

streamlit.write('The user entered ', fruit_choice)

# Normalize json data 

#display as a report
  
def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  
streamlit.header('Fruityvice fruit advice!')
try:
  fruit_choice = streamlit.text_input('what fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
#      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#      streamlit.dataframe(fruityvice_normalized)
      
except URLError as e:
  streamlit.error()
#import snowflake.connector
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()

streamlit.header("View Our Fruit List--Add yoiur Favourites!")
# Snowflake-related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  my_cnx.close()
  streamlit.dataframe(my_data_rows)
  
#my_cur.execute("SELECT * from fruit_load_list")
# my_data_row = my_cur.fetchall()
#streamlit.header("The fruit load list contains:")
#streamlit.dataframe(my_data_row)
#Allow the end user to add the fruit to the list
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values ('"+new_fruit+ "')")
    return "Thanks for adding "+ new_fruit
Add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(Add_my_fruit)
  my_cnx.close()
  streamlit.text(back_from_function)
# streamlit.write('Thanks for adding', Add_my_fruit)

# my_cur.execute("insert into fruit_load_list values ('from streamlit')")

