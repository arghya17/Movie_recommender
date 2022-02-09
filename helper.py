from jina import Client,Document
from config import TEXT_PORT,TEXT_SERVER,TOP_k,MODEL,CACHE_DIR,WORKSPACE_DIR
from jina import DocumentArray,Flow
import sys,os
import requests
from data_extractor import movies

flow = (
    Flow()
    .add(
        uses="jinahub://SpacyTextEncoder",
        uses_with={"model_name": MODEL},
        name="encoder",
        volumes=f"{CACHE_DIR}:/root/.cache",
        install_requirements=True,
    )
    .add(
        uses="jinahub+docker://SimpleIndexer",
        uses_metas={"workspace": "workspace"},
        volumes=f"./{WORKSPACE_DIR}:/workspace/workspace",
        name="indexer",
    )
)
def index():
    with flow:
        flow.index(
            inputs=movies,
            show_progress=True
        )


def search_by_text(input, server=TEXT_SERVER, port=TEXT_PORT, limit=TOP_k):
    client= Client(host=server, protocol="http", port=port)
    response=client.search(
        Document(text=input),
        parameters={"limit": limit},
        return_results=True,
        show_progress=True,
    )
    print(response)
    matches=response[0].data.docs[0].matches

    return matches

# def search(input, server=TEXT_SERVER, port=TEXT_PORT, limit=TOP_k):
#     with flow:
#         flow.protocol="http"
#         flow.port_expose=port
#         response=flow.search(
#             Document(text=input),
#             parameters={"limit": limit},
#             return_results=True,
#             show_progress=True,
#         )
#     matches=response[0].data.docs[0].matches
#     return matches

def get_matches(input):

    PORT = 8051
    ENDPOINT = "/search"

    url = f"http://0.0.0.0:{PORT}{ENDPOINT}"
    headers = {"Content-Type": "application/json"}

    data = {"data": [{"text": input}]}
    print(data)

    try:
        response = requests.post(url, headers=headers, json=data)
        content = response.json()
        print(response)
        return content["data"]["docs"][0]["matches"]
    except Exception:
        return []
#note index, search and get_matches are redundant and were used in previous versions of code
#The above mentioned functions do not affect the backend part of code in any way
"""text=input("Enter a search term : ")
matches=search(text)
for match in matches:
    print(f'-{match.text}')"""