import streamlit as st
from template import Template

contact = Template('Contact')
st.markdown(
    'Hey!! If you find me interested, contact me on [Zalo](https://zalo.me/0325808700) or [Facebook](https://www.facebook.com/profile.php?id=100024994269437).')


@st.experimental_singleton
def contact():
    from PIL import Image
    st.image('media/ZaloQR.jpg', caption='Zalo me')


    contact()
