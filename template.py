import streamlit as st


class Template:
    @staticmethod
    def __init__(page_title=None, page_icon=None):
        st.set_page_config(
            page_title=page_title,
            page_icon=page_icon,
            layout='wide'
        )
        # hide_st_style
        # header {visibility: hidden;}
        st.markdown("""
                <style>
                #MainMenu {visibility: hidden;}
                
                footer {visibility: hidden;}
                </style>
                """, unsafe_allow_html=True)
        
        st.title(page_title)
        st.sidebar.title('About')
        st.sidebar.info('GitHub repository: <https://github.com/J-Reacher/Sm>')
