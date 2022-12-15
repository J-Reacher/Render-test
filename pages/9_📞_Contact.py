import streamlit as st
from utils.template import Template

contact = Template('Contact')


@st.experimental_singleton
def contact():
    from PIL import Image

    image = Image.open('images/ZaloQR.jpg')
    st.image(image, caption='Zalo me')


if __name__ == '__main__':
    try:
        contact()
    except KeyboardInterrupt:
        st.text('Stopping')
