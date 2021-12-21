from jina import Document,DocumentArray, Flow
from data_extractor import movies

flow = (
    Flow()
    .add(
        uses="jinahub://SpacyTextEncoder",
        uses_with={"model_name": "en_core_web_md"},
        name="encoder",
        install_requirements=True
    )
    .add(
        uses="jinahub+docker://SimpleIndexer",
        uses_metas={"workspace": "workspace"},
        volumes="./workspace:/workspace/workspace",
        name="indexer",
    )
)

with flow:
    flow.index(inputs=movies)
    query = Document(text=input("Please enter your search term: "))
    response = flow.search(inputs=query, return_results=True)

def print_search_results(response):
    matches = response[0].data.docs[0].matches

    print("\nYour search results")
    print("-------------------\n")

    for match in matches:
        print(f"- {match.text}")

print_search_results(response)