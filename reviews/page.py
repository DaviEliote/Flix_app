import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
from reviews.service import ReviewService


def showReviews():

    reviews_service = ReviewService()
    reviews = reviews_service.get_review()

    if reviews:
        st.title('Reviews List')
        reviews_df = pd.json_normalize(reviews)
        sort= AgGrid(
            data= reviews,
            reload_data= True,
            key = 'Reviews_grid',

        )
    else:

        st.warning('Nenhuma avaliação encontrada')
    
    
        