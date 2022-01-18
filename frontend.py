import streamlit as st
from config import TEXT_PORT, TEXT_SERVER
from helper import search_by_text,search


matches=[]
st.set_page_config(page_title="Jina Movie Recommender")

st.header('Movie Recommender')
#function calling area

query=st.text_input("Enter Search term",key="text_search_box")
if st.button("Search", key="text_search"):
    matches=search(input=query, server=TEXT_SERVER,port=TEXT_PORT)

cell1,cell2,cell3=st.columns(3)
cell4,cell5,cell6=st.columns(3)
cell7,cell8,cell9=st.columns(3)

all_cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9]

for cell,match in zip(all_cells,matches):
    cell.text(match.text)