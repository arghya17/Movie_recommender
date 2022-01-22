from jina import Document,DocumentArray, Flow
import sys,os,inspect
from config import CACHE_DIR,MODEL, PORT,WORKSPACE_DIR


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 
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



def main():
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

    with flow as f:
        f.post(on="/index", inputs=movies, show_progress=True)
        #f.post(on="/search", inputs=movies, show_progress=True, on_done=check_query)
        f.protocol = "http"
        flow.port_expose=PORT
        f.cors = True
        f.block()


if __name__ == "__main__":
    main()

