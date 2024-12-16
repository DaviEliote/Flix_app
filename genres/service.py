import streamlit as st
from genres.repository import GenreRepository


class GenreService:

    def __init__(self):
        self.genre_repository = GenreRepository()


    def get_genre(self):
        # small cash to improve performance and API request overhead ;)
        if "genres" in st.session_state:
            return st.session_state.genres
        genres = self.genre_repository.get_genre()
        st.session_state.genres = genres
        return genres
    

    def create_genre (self, name):

        genre = dict (
            name=name,
        )
        new_genre = self.genre_repository.create_genre(genre)
        st.session_state.genres.append(new_genre)
        return new_genre