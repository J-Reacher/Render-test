# streamlit_app.py
import streamlit as st


def home():
    st.title('Home')
    from Pages.home import home_page
    st.balloons()
    home_page()


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


def matplot():
    st.title('Matplot')
    from Pages.matplot import matplot_page
    matplot_page()


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
    st.sidebar.markdown("""
                        If you find me interested, contact me on [Zalo](https://zalo.me/0325808700)
                         of [Facebook](https://www.facebook.com/profile.php?id=100024994269437)
                        """)
    st.sidebar.image('media/ZaloQR.jpg', caption='Zalo me')


if __name__ == '__main__':
    from streamlit_option_menu import option_menu as om

    st.set_page_config(
        page_title='Nhat Nam',
        page_icon=':green_heart:',
        layout='wide',
    )
    sidebar()

    pages = ['Home', 'Data', 'Matplot', 'Gallery']
    page_icons = ['house', '', '', '']
    selected_page = om(None, pages, icons=page_icons, orientation='horizontal')
    if selected_page == 'Home':
        home()
    if selected_page == 'Data':
        data()
    if selected_page == 'Matplot':
        matplot()
    if selected_page == 'Gallery':
        gallery()
