import requests 
import streamlit as st
from login.service import logout


class ActorRepository:

    def __init__(self):

        self.__base_url = 'https://davieliote.pythonanywhere.com/api/v1/'
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization' : f'Bearer {st.session_state.token}'
        }

    def get_actors(self):

        response = requests.get(
            self.__actors_url,
            headers = self.__headers

        )
        if response.status_code == 200:
            return response.json()

        if response.status_code == 401:
            st.warning("Erro ao buscar dados da API")

            return None
        raise Exception (f"Erro ao obter dados da API: {response.status_code}")
    

    def create_actor(self, actor):

        response = requests.post (
            self.__actors_url,
            headers= self.__headers,
            data= actor
        )
        if response.status_code == 201:
            return response.json()
        
        if response.status_code == 401:
            st.rerun
            return None
        
        raise Exception ( f"Erro ao enviar dados para API {response.status_code}")