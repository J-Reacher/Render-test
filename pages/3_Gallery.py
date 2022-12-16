import streamlit as st
from utils import Template

gallery = Template('Gallery')


@st.experimental_singleton
def Gallery():
    st.image('media/doan_duong.jpg', caption='Đoạn đường ta đã qua')
    st.image('media/nam_tay.jpg', caption='Vẫn có em ở lại')


if __name__ == '__main__':
    Gallery()
