import streamlit as st
from utils.hide_st_style import hide


class Template:
    @staticmethod
    def __init__(page_title=None, page_icon=None):
        st.set_page_config(
            page_title=page_title,
            page_icon=page_icon,
            layout='wide'
        )
        hide()
        st.title(page_title)
        st.sidebar.title('About')
        st.sidebar.info('GitHub repository: <https://github.com/J-Reacher/Sm>')
