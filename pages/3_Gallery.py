def Gallery():
    from utils.hide_st_style import hide

    from PIL import Image

    page_title = 'Gallery'

    st.set_page_config(page_title=page_title,)
    st.title(page_title)
    hide()

    image0 = Image.open('images/doan_duong.jpg')
    st.image(image0, caption='Đoạn đường ta đã qua')
    
    image1 = Image.open('images/nam_tay.jpg')
    st.image(image1, caption='Vẫn có em ở lại')    

if __name__ == '__main__':
    try:
        import streamlit as st
        Gallery()
    except KeyboardInterrupt:
        st.write('Stopping')
