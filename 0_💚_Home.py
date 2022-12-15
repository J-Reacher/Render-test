import streamlit as st
from utils.hide_st_style import hide

page_title = 'Home Page'
page_icon = '💚'

st.set_page_config(
    page_title=page_title,
    page_icon=page_icon
)
st.title(page_title)

hide()


@st.experimental_singleton
def homepage():
    st.markdown("""
                Nothing here yet!!
                """
                )


st.sidebar.success(page_title)

if __name__ == '__main__':
    try:
        homepage()
    except KeyboardInterrupt:
        st.text('Stopping')
