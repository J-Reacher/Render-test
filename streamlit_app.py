# streamlit_app.py

import hydralit as hy
import hydralit_components as hc
import streamlit as st

# For open link
import webbrowser

hc.nav_bar(menu_definition=None, sticky_nav=True)

app = hy.HydraApp(title='Nhat Nam', navbar_animation=False)


@app.addapp(title='Home', icon='🏡', is_home=True)
def home():
    st.title('Home')
    from Pages.home import home_page
    st.balloons()
    home_page()


@app.addapp(title='Data')
def data():
    st.title('Data')
    from Pages.data import sep, execute, example, menu
    
    execute()
    sep()

    if st.button('Examples'):
        st.markdown("A connection test with MySQL remote server")
        example()
    sep()

    menu()


@app.addapp(title='Matplot')
def matplot():
    st.title('Matplot')
    from Pages.matplot import matplot_page
    matplot_page()


@app.addapp(title='Gallery')
def gallery():
    st.title('Gallery')
    from Pages.gallery import gallery_page
    st.snow()
    gallery_page()


def sidebar():
    # hide_st_style
    # header {visibility: hidden;}
    #
    st.markdown("""
                <style>
                #MainMenu {visibility: hidden;}
                
                footer {visibility: hidden;}
                </style>
                """, unsafe_allow_html=True)

    st.sidebar.title('About')
    st.sidebar.info('GitHub repository: <https://github.com/J-Reacher/Sm>')

    if st.sidebar.button('Clear all caches'):
        st.experimental_memo.clear()
        st.experimental_singleton.clear()

    # Contact information
    st.sidebar.title('Contact')
    col1, col2 = st.columns(2)
    with col1:
        if st.sidebar.button('Zalo'):
            webbrowser.open('https://zalo.me/0325808700')
    with col2:
        if st.sidebar.button('Facebook'):
            webbrowser.open(
                'https://www.facebook.com/profile.php?id=100024994269437')
    st.sidebar.image('media/ZaloQR.jpg', caption='Zalo me')


if __name__ == '__main__':
    sidebar()
    app.run()
