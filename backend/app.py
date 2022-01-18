from jina import Document,DocumentArray, Flow
import sys,os
from config import CACHE_DIR,MODEL, PORT,WORKSPACE_DIR
import click


sys.path.insert(0,'/path/to/Movie_recommender')
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
            show_progress=True,
        )

def search():
    with flow:
        flow.protocol="http"
        flow.port_expose=PORT
        flow.block()

@click.command()
@click.option(
    "--task",
    "-t",
    type=click.Choice(["index", "search"], case_sensitive=False),
)
@click.option("--num_docs", "-n")
def main(task: str):
    if task == "index":
        index()
    elif task == "search":
        search()
    else:
        print("Please add '-t index' or '-t search' to your command")


if __name__ == "__main__":
    main()

