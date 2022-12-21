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

    col1, col2 = st.columns(2)
    with col1:
        your_codes = st.text_area('Codes you type below will be executed directly:',
                                  "st.write(':sunny: Nam has a :snake: pet in his backyard')")
        if st.button('Execute'):
            try:
                eval(your_codes)
            except SyntaxError:
                st.warning('Syntax error')
    with col2:
        if st.button('Examples'):
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

    if st.button('Clear all caches'):
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
    for page in pages:
        if selected_page == page:
            eval(f'{page.lower()}()')
