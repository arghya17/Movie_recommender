import streamlit as st
from config import TEXT_PORT, TEXT_SERVER
from helper import search_by_text,search,get_matches


matches=[]
st.set_page_config(page_title="Jina Movie Recommender")

st.header('Movie Recommender',)
#function calling area

query=st.text_input("Enter Search term",key="text_search_box")
if st.button("Search", key="text_search"):
    matches=search_by_text(input=query,server=TEXT_SERVER, port=TEXT_PORT)
    print(matches)#print just for debugging
st.subheader("Recommendations are:")
for match in matches:
    value=f"##### {match.tags.fields['Title'].string_value}"
    value=value+f"\nSummary : {match.tags.fields['Short Summary'].string_value}\n"
    value=value+f"\nGenre : {match.tags.fields['Genres'].string_value}  "  
    value=value+"  "+f"*[Youtube Trailer](https://www.youtube.com/watch?v={match.tags.fields['YouTube Trailer'].string_value})*"
    print(value)
    st.write(value)
