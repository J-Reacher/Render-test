import streamlit as st


def print_csv():
    import pandas as pd
    _data = './data.csv'
    st.write(pd.read_csv(_data))


def append_csv():
    import csv

    _append = (int(st.sidebar.number_input('ID: ')),  # 8 attributes
               st.sidebar.text_input('Name: '),
               st.sidebar.text_input('Major: '),
               st.sidebar.date_input('Date of birth (yyyy-mm-dd): '),
               st.sidebar.text_input('Course (yyyy-yyyy): '),
               st.sidebar.number_input('Remaining tuition fees: $'),
               st.sidebar.checkbox('In the dormitory '),
               st.sidebar.text_input('Address: ')
               )
    st.write(_append)

    to_file = st.sidebar.button('Write to file')
    if to_file:
        _data = './data.csv'
        with open(_data, 'a', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(_append)


def main():
    from streamlit_option_menu import option_menu as om

    st.title('Student Management')
    choice = om('Main menu', ['Print', 'Append', ],
                default_index=0, orientation='horizontal')
    if choice == 'Print':
        print_csv()
    elif choice == 'Append':
        append_csv()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nStopped')
