import requests
from bs4 import BeautifulSoup
import streamlit as st

from template import Template

home = Template('Home')


@st.experimental_memo
def apod():
    url = 'https://apod.nasa.gov/apod/'
    
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    images = soup.find_all('img')
    for image in images:
        name = image['alt']
        link = image['src']
    st.header('Astronomy Picture of the Day')    
    st.image(f'{url}{link}', caption=name)


@st.experimental_singleton(suppress_st_warning=True)
def home():
    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        apod()
    
    with col2:
        st.header("""
                    Welcome to my website!!
                    """)
        st.info('The menu is located at top-left ↖ corner')
        st.video('https://youtu.be/beACOLaYtkM')
        
if __name__ == '__main__':
    st.balloons()
    home()
    
