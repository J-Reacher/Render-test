import streamlit as st
from utils.template import Template

home = Template('Home')
home.markdown(
    'Hello, wellcome to my website!!, the menu is located at top-left ↖ corner')


def home():
    st.video('media/hanhtrinh_2ngay1dem.mp4')


if __name__ == '__main__':
    try:
        home()
    except KeyboardInterrupt:
        st.text('Stopping')
