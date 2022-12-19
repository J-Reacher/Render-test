# streamlit_app.py

import streamlit as st
import hydralit as hy


app = hy.HydraApp(title='Nhat Nam',)


@app.addapp(is_home=True)
def Home():
    st.title('Home')
    from Pages.home import home_page
    st.balloons()
    home_page()


@app.addapp()
def Data():
    st.title('Data')
    from Pages.data import sep, execute, example, menu
    execute()
    sep()

    st.markdown("A connection test with MySQL remote server")
    example()
    sep()

    menu()


@app.addapp()
def Matplot():
    st.title('Matplot')
    from Pages.matplot import matplot_page
    matplot_page()


@app.addapp()
def Gallery():
    st.title('Gallery')
    from Pages.gallery import gallery_page
    st.snow()
    gallery_page()


@app.addapp()
def Contact():
    st.title('Contact')
    from Pages.contact import contact_page
    contact_page()


if __name__ == '__main__':
    # hide_st_style
    # header {visibility: hidden;}
    # #MainMenu {visibility: hidden;}
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
