import streamlit as st
from utils.template import Template

contact = Template('Contact')
contact.markdown(
    'Hey!! If you find me interested, contact me on [Zalo](https://zalo.me/0325808700) or [Facebook](https://www.facebook.com/profile.php?id=100024994269437).')


@st.experimental_singleton
def contact():
    from PIL import Image
    st.image('media/ZaloQR.jpg', caption='Zalo me')


if __name__ == '__main__':
    try:
        contact()
    except KeyboardInterrupt:
        st.text('Stopping')
