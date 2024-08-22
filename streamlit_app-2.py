# Import python packages
import streamlit as st
import snowflake.snowpark.context
from snowflake.snowpark.context import get_active_session

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :cup_with_straw:")
st.write(
    """
    Choose the fruit you want in your customised smoothie 
    """
)

order_name = st.text_input('Name on Smoothie : ')
st.write('Name on smoothie will be : ' , order_name)


from snowflake.snowpark.functions import col
session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select(col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(

    'Choose upto 5 ingredients:' , my_dataframe
)
if ingredients_list :
    ingredients_string = ''
    for fruits in ingredients_list:
        ingredients_string += fruits + ' '
    st.write(ingredients_string)
    insert_statment = """ insert into smoothies.public.orders(name_on_order , ingredients)
            values ('""" + order_name + """ ','""" + ingredients_string + """')"""

    #st.write(insert_statent)
    submit_button = st.button('Submit')
    
    if submit_button :
        session.sql(insert_statment).collect()
        st.success('Your Smoothie is ordered!', icon="✅")











