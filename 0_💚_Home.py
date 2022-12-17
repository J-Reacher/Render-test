import streamlit as st
from utils import Template

home = Template('Home')

@st.experimental_singleton
def home():
    column1, column2, column3 = st.columns(3)
    with column1:
        st.markdown("""
                    Welcome to my website, the menu is located at top-left ↖ corner
                    """)
    with column2:
        st.markdown('## Hello!!')
    with column3:
        st.markdown('💚💚💚')
        
        
if __name__ == '__main__':
    st.balloons()
    home()
    st.video('https://youtu.be/beACOLaYtkM')
