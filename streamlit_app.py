import streamlit
import pandas
streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and blueberry meal')
streamlit.text('🥗Kale, Spinach and rocket smoothie')
streamlit.text('🐔Hard-Boiled free-range eggs')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#using pandas data frame
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list = my_fruit_list.set_index('Fruit')

#streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
#streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

#Display on list of items
#streamlit.dataframe(my_fruit_list)

#We'll ask our app to put the list of selected fruits into a variable called fruits_selected. Then, we'll ask our app to use the fruits in our fruits_selected list 
#to pull rows from the full data set (and assign that data to a variable called fruits_to_show). Finally, we'll ask the app to use the data in fruits_to_show in the dataframe it displays on the page. 
fruits_selected = streamlit.multiselect("pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
