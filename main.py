import streamlit as st

st.title("Movie Recommender")
text=st.text_input("Enter Keyword for search",key="Input")
print(text)
st.button("Search")