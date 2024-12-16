



import streamlit as st


def showVideo():
    title = st.title("BEM VINDO AO FLIX APP")
    video = st.video('images/homevideo.mp4', autoplay=True, loop=True)
    

    return video