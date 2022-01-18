from http import client
from jina import Client,Document
from config import TEXT_PORT,TEXT_SERVER,TOP_k,MODEL,CACHE_DIR,WORKSPACE_DIR
from jina import DocumentArray,Flow
import sys
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

index()
def search_by_text(input, server=TEXT_SERVER, port=TEXT_PORT, limit=TOP_k):
    client= Client(host=server, protocol="http", port=port)
    response=client.search(
        Document(text=input),
        parameters={"limit": limit},
        return_results=True,
        show_progress=True,
    )
    matches=response[0].data.docs[0].matches

    return matches

def search(input, server=TEXT_SERVER, port=TEXT_PORT, limit=TOP_k):
    with flow:
        flow.protocol="http"
        flow.port_expose=port
        response=flow.search(
            Document(text=input),
            parameters={"limit": limit},
            return_results=True,
            show_progress=True,
        )
    matches=response[0].data.docs[0].matches

    return matches

"""text=input("Enter a search term : ")
matches=search(text)
for match in matches:
    print(f'-{match.text}')"""