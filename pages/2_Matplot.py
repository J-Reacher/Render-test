def Matplot():
    import matplotlib.pyplot as plt
    import numpy as np

    from utils.hide_st_style import hide

    page_title = 'Matplot'
    
    st.set_page_config(page_title=page_title,)
    st.title(page_title)
    hide()

    # create 1000 equally spaced points between -10 and 10
    x = np.linspace(-10, 10, 1000)

    # calculate the y value for each element of the x vector
    y = (x ** 2 / 9)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    st.pyplot(fig)


if __name__ == '__main__':
    try:
        import streamlit as st
        Matplot()
    except KeyboardInterrupt:
        st.text('Stopping')
