# streamlit_app.py
import streamlit as st


def home():
    st.title('Home')
    from Pages.home import home_page
    st.balloons()
    home_page()


def data():
    st.title('Data')
    from Pages.data import sep, example, menu

    if st.button('Examples'):
        example()
        sep()
    menu()


def gallery():
    st.title('Gallery')
    from Pages.gallery import gallery_page
    st.snow()
    gallery_page()


def sidebar():
    st.sidebar.title('About')
    st.sidebar.info('GitHub repository: <https://github.com/J-Reacher/Sm>')

    if st.sidebar.button('Clear all caches'):
        st.experimental_memo.clear()
        st.experimental_singleton.clear()

    # Contact information
    st.sidebar.title('Contact')
    st.sidebar.markdown("""
                        If you find me interested, contact me on
                         [Facebook](https://www.facebook.com/profile.php?id=100024994269437)
                         or [Zalo](https://zalo.me/0325808700).
                        """)
    st.sidebar.image('media/ZaloQR.jpg', caption='Zalo me')


if __name__ == '__main__':
    from streamlit_option_menu import option_menu as om

    st.set_page_config(
        page_title='Nhat Nam',
        page_icon=':green_heart:',
        layout='wide',
    )
    # hide_st_style
    # header {visibility: hidden;}
    #
    st.markdown("""
                    <style>
                    #MainMenu {visibility: hidden;}

                    footer {visibility: hidden;}
                    </style>
                    """, unsafe_allow_html=True)
    sidebar()

    pages = ['Home', 'Data', 'Gallery']
    page_icons = ['house', '', '', '']
    selected_page = om(None, pages, icons=page_icons, orientation='horizontal')
    for page in pages:
        if selected_page == page:
            eval(f'{page.lower()}()')
