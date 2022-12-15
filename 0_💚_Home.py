import streamlit as st
from utils.template import Template

home = Template('Home')


def home():
    column1, column2, column3 = st.columns(3)
    with column1:
        st.markdown(
            'Wellcome to my website, the menu is located at top-left ↖ corner')

    with column2:
        st.markdown('## Hello!!')
    with column3:
        st.markdown('💚💚💚')
    st.video('media/hanhtrinh_2ngay1dem.mp4')
    st.text('Hành trình 2 ngày 1 đêm với mn tại DH Khoa học Tự nhiên')


if __name__ == '__main__':
    try:
        home()
    except KeyboardInterrupt:
        st.text('Stopping')
