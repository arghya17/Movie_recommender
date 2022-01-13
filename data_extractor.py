from jina import Document, DocumentArray, Flow
from docarray.document.generators import from_csv

with open("Data.csv") as file:
    movies = DocumentArray(
        from_csv(file, field_resolver={'Movie Poster': 'uri', 'Summary': 'text'})
    )
    