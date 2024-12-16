import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from actors.service import ActorService
from genres.service import GenreService
from movies.service import MoviesService





def showMovies():

    movies_service = MoviesService()
    movies = movies_service.get_movies()

    if movies:
        st.title('Lista de filmes')
        movies_df = pd.json_normalize(movies)
        movies_df = movies_df.drop(columns=['actors', 'genre.id', 'rate'])
        sort= AgGrid(
            data= movies_df,
            reload_data= True,
            key = 'Movies_grid',

    )
    else:
        st.warning("Nenhum filme encontrado")
        

    st.title("Cadastrar novo filme")

    title = st.text_input('Titulo')

    genre_service = GenreService()
    genres = genre_service.get_genre()
    genre_names = { genre['name'] : genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))


    actor_service = ActorService()
    actors = actor_service.get_actor()
    actors_name = {actor['name']: actor['id'] for actor in actors}
    selected_actors_name = st.multiselect('Atores/Atrizes', list(actors_name.keys()))
    selected_actors_id = {actors_name[name] for name in selected_actors_name}

    description = st.text_area('Descricao')

    if st.button('Cadastrar'):

        new_movie = movies_service.create_movie(
            title=title,
            genre=genre_names[selected_genre_name],
            actors=selected_actors_id,
            description= description
        )
        if new_movie:
            st.rerun()

        else:
            st.error("Erro ao cadastrar filme")