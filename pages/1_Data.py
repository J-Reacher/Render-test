import streamlit as st
from utils.hide_st_style import hide

page_title = 'Data'

st.set_page_config(
    page_title=page_title,
)
st.title(page_title)

hide()


def print_csv():
    import pandas as pd
    _data = 'data.csv'
    st.write(pd.read_csv(_data))


def append_csv():
    import csv

    _append = (f"'{st.number_input('ID: ')}'",  # 8 attributes
               st.text_input('Name: '),
               st.text_input('Major: '),
               st.date_input('Date of birth (yyyy-mm-dd): '),
               st.text_input('Course (yyyy-yyyy): '),
               st.number_input('Remaining tuition fees: vnd'),
               st.checkbox('In the dormitory '),
               st.text_input('Address: ')
               )
    if to_file := st.button('Save'):
        _data = 'data.csv'
        with open(_data, 'a', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(_append)
        st.write(_append)
        st.success('Data saved!')


# @st.experimental_get_query_params
def Data():
    from streamlit_option_menu import option_menu as om

    choice = om('Main menu', ['Print', 'Append', ],
                default_index=0, orientation='horizontal')
    if choice == 'Print':
        print_csv()
    elif choice == 'Append':
        append_csv()


if __name__ == '__main__':
    try:
        Data()
    except KeyboardInterrupt:
        st.text('Stopping')
