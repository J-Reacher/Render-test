import streamlit as st


@st.experimental_singleton
def contact_page():
    col1, col2 = st.columns([0.2, 0.8])
    with col1:
        st.markdown(
            'Hey!! If you find me interested, contact me on [Zalo](https://zalo.me/0325808700) or [Facebook](https://www.facebook.com/profile.php?id=100024994269437).')

    with col2:
        st.image('media/ZaloQR.jpg', caption='Zalo me')
