from typing import Dict
from jina import Document, DocumentArray, Flow
from docarray.document.generators import from_csv
from random import randint

with open("Data.csv") as file:
    movies = DocumentArray(
        from_csv(file, field_resolver={'Summary': 'text'})
    )
movies=movies.shuffle(seed=randint)
for i in range(len(movies)):
    movies[i].text=movies[i].text+f"{movies[i].tags.fields['Genres'].string_value}"
print(movies[0].tags.fields['Title'].string_value)
#print is just an example to see the parameters of movies docArray