# streamlit_app.py

import streamlit as st
import hydralit as hy

app = hy.HydraApp(title='Simple Muliti_page App', navbar_animation=False,)


@app.addapp(is_home=True)
def Home():
    hy.info('Home')
    from pages.home import home_page
    st.balloons()
    home_page()


@app.addapp()
def Data():
    from pages.data import sep, execute, example, menu
    execute()
    sep()

    st.markdown("A connection test with MySQL remote server")
    example()
    sep()

    menu()


@app.addapp()
def Matplot():
    from pages.matplot import matplot_page
    matplot_page()


@app.addapp()
def Gallery():
    from pages.gallery import gallery_page
    st.snow()
    gallery_page()


@app.addapp()
def Contact():
    from pages.contact import contact_page
    contact_page()


if __name__ == '__main__':
    # hide_st_style
    # header {visibility: hidden;}
    # MainMenu {visibility: hidden;}
    st.markdown("""
            <style>
            
            
            footer {visibility: hidden;}
            </style>
            """, unsafe_allow_html=True)

    st.sidebar.title('About')
    st.sidebar.info('GitHub repository: <https://github.com/J-Reacher/Sm>')

    if st.sidebar.button('Clear all caches'):
        st.experimental_memo.clear()
        st.experimental_singleton.clear()

    app.run()
