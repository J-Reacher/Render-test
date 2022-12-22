import streamlit as st


def gallery_page():
    col1, col2 = st.columns([0.75, 0.275])
    with col1:
        st.image('media/doan_duong.jpg', caption='Đoạn đường ta đã qua')
    with col2:
        st.image('media/nam_tay.jpg', caption='Vẫn có em ở lại')

    col1, col2, = st.columns([0.340, 0.6])
    with col1:
        st.image('media/hoa_cuc.jpg')

    with col2:
        st.image('media/nang_chieu_qua_ke_la.jpg')
