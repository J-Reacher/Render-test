def main():
    from utils.hide_st_style import hide

    page_title = 'Test Page'

    st.set_page_config(page_title=page_title,)
    st.title(page_title)
    hide()


if __name__ == '__main__':
    try:
        import streamlit as st

        main()
    except KeyboardInterrupt:
        st.text('Stopping')
