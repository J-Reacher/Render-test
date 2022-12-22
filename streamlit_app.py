# streamlit_app.py
import streamlit as st


def data():
    st.title('Data')
    from Pages.data import menu

    col1, col2 = st.columns(2)
    with col1:
        st.info("""
                Student management using Python's module [Streamlit](https://streamlit.io/)
                  and
                 [MySQL](https://www.mysql.com/) hosted on [Free SQL database](https://www.freesqldatabase.com/)
                 """)
    with col2:
        st.info("""
                The emojis you've seen is available from
                [Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
                """)
    menu()


if __name__ == '__main__':
    data()
