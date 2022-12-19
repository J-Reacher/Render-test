import streamlit as st


class Template:
    @staticmethod
    def __init__(page_title=None, page_icon=None):
        st.set_page_config(
            initial_sidebar_state='collapsed',
            page_title=page_title,
            page_icon=page_icon,
            layout='wide'
        )
