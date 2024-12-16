import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from .service import GenreService






def showGenres():

    genre_service = GenreService()
    genres = genre_service.get_genre()
    print(genres)

    if genres:
        st.title('Lista de gêneros')
        genre_df = pd.json_normalize(genres)
        sort= AgGrid(
            data= genre_df,
            reload_data=True,
            key = 'genres_grid'

        )
    else:

        st.warning("Nenhum genero cadastrado")

    name = st.text_input(' add new genre' )
    if st.button("Cadastrar"):
        new_genre = genre_service.create_genre(

            name= name
        )
    
        if new_genre:
            st.rerun()
        else:
            st.warning("Erro ao cadastrar gênero. Verifique os campos")