import langchain_helper as lgc
import streamlit as st


st.title("Pets name genrator")

# Select the Animal type 
animal_type = st.sidebar.selectbox("What is your pet ?", ("Cat", "Cow", "Dog"))

# Select the color
if animal_type == "Cat":
    pet_color =st.sidebar.text_area(label="What is your Pet Color?", max_chars=10) 
if animal_type == "Cow":
    pet_color =st.sidebar.text_area(label="What is your Pet Color?", max_chars=10) 
if animal_type == "Dog":
    pet_color =st.sidebar.text_area(label="What is your Pet Color?", max_chars=10) 