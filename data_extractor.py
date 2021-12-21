from jina import Document, DocumentArray, Flow
from jina.types.document.generators import from_csv

with open("Data.csv") as file:
    movies= DocumentArray(from_csv(file))
