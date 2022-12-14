import streamlit as st

page_title = 'Home page'
page_icon = '💚'

st.set_page_config(
    page_title = page_title,
    page_icon = page_icon
)

st.title(page_title)
st.sidebar.success(page_title)
