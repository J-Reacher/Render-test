import streamlit as st


@st.experimental_singleton
def gallery_page():
    st.image('media/doan_duong.jpg', caption='Đoạn đường ta đã qua')
    st.image('media/nam_tay.jpg', caption='Vẫn có em ở lại')
