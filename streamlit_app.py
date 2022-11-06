import streamlit

streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Favorites')
streamlit.text(' OMega 3 and Blueberry OatMeal')
streamlit.text('🍌🥭 Idly and Dosa with Samber and Chutney')
streamlit.text('Pancake with Maple Syrup')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

