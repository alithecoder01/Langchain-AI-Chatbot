import langchain_helper as lgc
import streamlit as st


st.title("Pets name genrator")

# Select the Animal type 
user_animal_type = st.sidebar.selectbox("What is your pet ?", ("Cat", "Cow", "Dog"))

# Select the color
if user_animal_type == "Cat":
    user_pet_color =st.sidebar.text_area(label="What is your Pet Color?", max_chars=10) 
if user_animal_type == "Cow":
    user_pet_color =st.sidebar.text_area(label="What is your Pet Color?", max_chars=10) 
if user_animal_type == "Dog":
    user_pet_color =st.sidebar.text_area(label="What is your Pet Color?", max_chars=10) 

if user_pet_color :
    response = lgc.genratename(user_animal_type,user_pet_color)
    st.text(response["pet_name"])