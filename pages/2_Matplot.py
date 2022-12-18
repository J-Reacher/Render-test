import streamlit as st

from template import Template

matplot = Template('Matplot')


@st.experimental_singleton
def main():
    with st.echo():
        import matplotlib.pyplot as plt
        import numpy as np

        # create 1000 equally spaced points between -10 and 10
        x = np.linspace(-10, 10, 1000)

        # calculate the y value for each element of the x vector
        y = (x ** 2 / 9)

        fig, ax = plt.subplots()
        ax.plot(x, y)
        st.pyplot(fig)  # import streamlit as st


if __name__ == '__main__':
    main()
