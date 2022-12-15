import streamlit as st
from utils.hide_st_style import hide


class Template:
    def __init__(self=None, page_title=None, page_icon=None):
        st.set_page_config(
            page_title=page_title,
            page_icon=page_icon,
        )
        hide()
        st.title(page_title)
        st.sidebar.success(page_title)

    @staticmethod
    def markdown(markdown=None):
        st.markdown(f"""
                    {markdown}
                    """)
