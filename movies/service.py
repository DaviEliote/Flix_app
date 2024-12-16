from movies.repository import MoviesRepository
import streamlit as st



class MoviesService:

    def __init__(self):

        self.movies_repository = MoviesRepository()


    def get_movies(self):
        # small cash to improve performance and API request overhead ;)
        if 'movies' in st.session_state:
            return st.session_state.movies
        movies = self.movies_repository.get_movies()
        st.session_state.movies = movies
        return movies


    def create_movie(self, title, genre, actors, description):

        movie = dict (
            title = title,
            genre = genre,
            actors = actors,
            description = description
        )
        new_movie = self.movies_repository.create_movie(movie)
        st.session_state.movies.append(movie)
        return new_movie