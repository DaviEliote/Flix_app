import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from datetime import datetime
from actors.service import ActorService


def showActors():

    actor_service = ActorService()
    actors = actor_service.get_actor()

    if actors:
        st.title('Lista de atores')
        actors_df = pd.json_normalize(actors)
        sort= AgGrid(
            data= actors_df,
            reload_data= True,
            key = 'actors_grid',

        )   
    else :
        st.warning("Nenhum ator/atriz encontrados.")


    name = st.text_input(' Adicione um novo ator/atriz' )
    birthdate = st.date_input (
        label= "data de nascimento",
        value= datetime.today(),
        min_value= datetime(1600,1,1).date(),
        max_value=datetime.today(),
        format='DD/MM/YYYY'
    )
    nationality_dropdown = ['BRAZIL', 'USA']
    nationality = st.selectbox(
        label='nacionalidade', 
        options=nationality_dropdown)  

    if st.button("Cadastrar"):
        new_actor = actor_service.create_actor(
            name=name,
            birthdate=birthdate,
            nationality=nationality
        )
        if new_actor:
            st.rerun()
        else:
            st.error( f" Erro ao cadastrar ator/atriz. Verifique os campos ")
    
        