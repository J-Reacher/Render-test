# streamlit_app.py
import streamlit as st


def home():
    st.title('Home')
    from Pages.home import home_page
    home_page()


def data():
    st.title('Data')
    from Pages.data import sep, example, menu

    st.info("""
            Student management using Python's module [Streamlit](https://streamlit.io/)
              and
             [MySQL](https://www.mysql.com/) hosted on [Free SQL database](https://www.freesqldatabase.com/)
             """)
    st.info("""
            The emojis you've seen is available from
            [Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
            """)

    if st.button('Examples'):
        example()
        sep()
    menu()


def sidebar():
    st.sidebar.title('About')
    st.sidebar.info('GitHub repository: <https://github.com/J-Reacher/Sm>')

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
    sidebar()

    pages = ['Home', 'Data']
    page_icons = ['house', '', '']
    selected_page = om(None, pages, icons=page_icons, orientation='horizontal')
    for page in pages:
        if selected_page == page:
            eval(f'{page.lower()}()')
