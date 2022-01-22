import streamlit as st
from config import TEXT_PORT, TEXT_SERVER
from helper import search_by_text,search,get_matches


matches=[]
st.set_page_config(page_title="Jina Movie Recommender")

st.header('Movie Recommender')
#function calling area

query=st.text_input("Enter Search term",key="text_search_box")
if st.button("Search", key="text_search"):
    matches=search_by_text(input=query,server=TEXT_SERVER, port=TEXT_PORT)
    print(matches)

for match in matches:
    st.write(match.text)