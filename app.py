import streamlit as st


def print_csv():
    import pandas as pd
    _data = './data.csv'
    st.write(pd.read_csv(_data))


def append_csv():
    import csv

    _append = (st.number_input('ID: '),  # 8 attributes
               st.text_input('Name: '),
               st.text_input('Major: '),
               st.date_input('Date of birth (yyyy-mm-dd): '),
               st.text_input('Course (yyyy-yyyy): '),
               st.number_input('Remaining tuition fees: $'),
               st.checkbox('In the dormitory '),
               st.text_input('Address: ')
               )
    st.write(_append)

    if to_file := st.button('Write to file'):
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
