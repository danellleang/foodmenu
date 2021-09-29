import streamlit as st
from binarysearchtree import foodMenu
import pandas as pd

if 'hasFood' not in st.session_state:
    st.session_state.hasFood = 0


st.header("Welcome to Danell's court Food Menu Demo")

st.write("Choose an option from the radio button on the side bar to continue.")


option = st.sidebar.selectbox(
    'Select an option',
     ['Add a food','Find a food','Get the sorted food list','Reset entire food menu system','Contact us'])

if option == 'Add a food':
    foodName = st.text_input("Please enter the food name")
    foodPrice = st.text_input("Please enter the food price in RM")
    submit = st.button('submit')

    if submit:

        if foodName != "" and foodPrice !="":

            if st.session_state.hasFood==1:

                st.session_state.RBAFoodMenu.addNode(foodName,foodPrice)
                st.write("[{} , RM {}] has been added to the food Menu.".format(foodName, foodPrice))
            
            else:
                st.session_state.RBAFoodMenu = foodMenu(foodName,foodPrice)
                st.write("[{} , RM {}] has been added to the food Menu.".format(foodName, foodPrice))
                st.session_state.hasFood = 1

        else:
            st.write("Please fill in the details first! ")


elif option == 'Find a food':
        

    if st.session_state.hasFood ==1:

        foodName = st.text_input("Please enter the food name that you want to search for")
        
        st.write("The food is in the Food Menu: {}".format(st.session_state.RBAFoodMenu.findNode(foodName)))
 

    else:
        st.write("Empty Food Menu.")


    
elif option == 'Get the sorted food list':

    if st.session_state.hasFood ==1:
        st.write("The list in the Food Menu:")
        st.write(pd.DataFrame(st.session_state.RBAFoodMenu.inOrderTraversal(),columns=["Food Name", "Price"]))


        st.write("Empty Food Menu.")

        
 elif option == 'Reset entire food menu system':
    st.write("The food menu system has been reset.")

    st.session_state.hasFood = 0 
    st.session_state.RBAFoodMenu = []

        
  else:
         st.write("Please email your query to tech_support@dc.com or call us via +603-23008888")         

