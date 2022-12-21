import requests
import streamlit as st
from bs4 import BeautifulSoup


# Get the image and its alternative text from apod
@st.experimental_memo
def apod():
    url = 'https://apod.nasa.gov/apod/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.find_all('img')

    src = None
    for image in images:
        src = image['src']
    st.header('Astronomy Picture of the Day')
    st.info(f'[Original Image]({url})')
    st.image(f'{url}{src}')


def home_page():
    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        apod()

    with col2:
        st.header("Welcome to my website!!")
        st.markdown('A short yet memorable time to me')
        st.markdown(
            'Editor: [Dan Khanh](https://www.facebook.com/nangva.mua.908)')
        st.video('https://youtu.be/beACOLaYtkM')
