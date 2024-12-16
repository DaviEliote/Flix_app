import streamlit as st

from genres.page import showGenres
from actors.page import showActors
from movies.page import showMovies
# from reviews.page import showReviews
from login.page import show_login
from images.display import showVideo





import streamlit.components.v1 as components





if 'token' not in st.session_state:
        show_login()
else:
        

        
        option= st.sidebar.selectbox ( 
            'select one option',
            ['inicio', 'gêneros', 'atores', 'filmes',]
        )
        
        if option =='inicio':
          
            showVideo()
            st.info("""Este é um sistema que consulta uma API externa desenvolvida por mim mesmo, e que atualiza e insere dados em tempo real,
                     com um pequeno sistema de cashing, para melhorar o desempenho e     overheading na API""")
            st.feedback('faces')


        if option == 'gêneros':
            showGenres()


        if option == 'atores':
            showActors()
            ...
        if option == 'filmes':
            showMovies()
            


