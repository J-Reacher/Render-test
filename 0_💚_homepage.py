def main():
    page_title = 'Home page'
    page_icon = '💚'

    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon
    )

    st.title(page_title)
    st.sidebar.success(page_title)
    
    hide()
    
    st.markdown("""
                Nothing here yet!!
                """
    )


if __name__ == '__main__':
    try:
        import streamlit as st
        from utils.hide_st_style import hide

        main()
    except KeyboardInterrupt:
        st.text('Stopping')
