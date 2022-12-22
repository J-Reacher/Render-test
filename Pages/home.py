import requests
import streamlit as st
from bs4 import BeautifulSoup


def apod():
    url = 'https://apod.nasa.gov/apod/'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.find_all('img')

    src = None
    alt = None
    for image in images:
        src = image['src']
        alt = image['alt']
    st.header('Astronomy Picture of the Day')
    st.info(f'[Original Image]({url})')
    st.image(f'{url}{src}', caption=alt)


def home_page():
    col1, col2, col3 = st.columns(3)
    with col1:
        apod()
        st.image('media/nang_chieu_qua_ke_la.jpg')

    with col2:
        st.video('https://youtu.be/beACOLaYtkM')
        st.markdown('Editor: [Dan Khanh](https://www.facebook.com/nangva.mua.908)')

        st.image('media/hoa_cuc.jpg')

    with col3:
        st.image('media/doan_duong.jpg', caption='Đoạn đường ta đã qua')
        st.image('media/nam_tay.jpg', caption='Vẫn có em ở lại')
