import streamlit
streamlit.title ("My Parents New Healthy Diner👌👌👌")
streamlit.header("Breakfast Menu✍")
streamlit.text(" Oatmeal")
streamlit.text("salads🥗🥛")
streamlit.text("Bread and Milk🥛")

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


steamlit.multiselect( list(my_fruit_list.index(1)))



