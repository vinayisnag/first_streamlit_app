import streamlit

streamlit.title('My Parents new healthy diner')

streamlit.header('Breakfast Favorites')
streamlit.text(' OMega 3 and Blueberry OatMeal')
streamlit.text('🍌🥭 Idly and Dosa with Samber and Chutney')
streamlit.text('Pancake with Maple Syrup')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

