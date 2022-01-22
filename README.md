# Movie_recommender

A Movie recommender website based on neural search built using jina as backend and streamlit as frontend

Dataset from [this site](https://data.world/iliketurtles/movie-dataset/workspace/file?filename=Hydra-Movie-Scrape.csv). Movies are updated upto year 2018

##Idea:
Search for movie recommendation using any keyword

##Tech used?
Backend: Jina
Frontend: Streamlit

##How to use?
Clone the repository in the local machine
-Create a new virtual environment in python

```
python -m venv movie
```

Switch to the new virtual environment

```
source movie/bin/activate
```

Download the requirements

```
pip install -r requirements.txt
```

Run the backend that is the server:

```
python -u backend/app.py
```

Lauch the frontend, in another terminal:

```
streamlit run frontend.py
```

Upon executing the above commands a local host will be launched in your default browser or else head over to `http://localhost:8501` to search your favorite movies for watchlist.

##Few things to note:
-After running the program once an workspace folder will be created. Note before running the program again delete the workspace folder
-To update movies only change DocumentArray in data_extractor.py
