def main():
    hide()
    
    
if __name__ == '__main__':
    try:
        import streamlit as st
        from utils.hide_st_style import hide
        
        main()
    except KeyboardInterrupt:
        st.text('Stopping')