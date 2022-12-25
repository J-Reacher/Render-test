# streamlit_app.py

import mysql.connector
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu as om


def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])


connection = init_connection()


def run_query(query: str):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


def tables() -> list[str]:
    return [i[0] for i in run_query('SHOW TABLES;')]


table_names = tables()


# Function that returns the table's column names
def table_col_names(table_name: list[str]) -> list[str]:
    return [row[0] for row in run_query(f"SHOW COLUMNS FROM {table_name};")]


def table_col_types(table_name: list[str]) -> list[str]:
    return [row[1] for row in run_query(f"SHOW COLUMNS FROM {table_name};")]


def example(table_name: list[str]):
    st.markdown('Students:')
    df = pd.DataFrame(
        run_query(f"""
        SELECT 
         StudentID, Name, Major, DOB,
         Course, Remaining_fee, In_dormitory, Address
         FROM {table_name};
        """),
        columns=table_col_names(table_name)
    )
    st.dataframe(df)


def menu():
    # Query directly from the web
    the_query = st.text_area('Optional query:', """SELECT name, pet \nFROM Pets \nWHERE name = N'Aries';""")
    if st.button('Query'):
        df = pd.DataFrame(run_query(the_query))
        st.dataframe(df)
        connection.commit()

    st.markdown('---')

    example(['Students', ])

    options = ['Insert', 'Update', 'Delete']
    choice = om(None, options, orientation='horizontal')
    match choice:
        case 'Insert':
            _insert()
        case 'Update':
            _update()
        case 'Delete':
            _delete()


def _insert():
    table_name = st.selectbox('Table name:', table_names)
    match table_name:
        case 'Students':
            with st.form('Students'):
                student_id = st.number_input('StudentID:')  # 8 eight attributes
                student_name = st.text_input('Name:')
                major = st.text_input('Major:')
                dob = st.date_input('DOB:')
                learning_course = st.date_input('Course:').year
                fees = st.number_input('Remaining fees:')
                dormitory = st.radio('In dormitory?', ['No', 'Yes'])
                address = st.text_area('Address')

                if st.form_submit_button('Submit'):
                    run_query(f"""
                            INSERT INTO
                                {table_name}
                            VALUES
                                ('{student_id}', '{student_name}', '{major}', '{dob}',
                                '{learning_course}', '{fees}', '{dormitory}', '{address}');
                            """)
                    connection.commit()
                    st.success('Inserted')

        case 'Pets':
            with st.form('Pets'):
                name = st.text_input('Name:')
                pet = st.text_input('Pet:')

                if st.form_submit_button('Submit'):
                    run_query(f"""
                            INSERT INTO
                                {table_name}
                            VALUES
                                ('{name}', '{pet}');
                            """)
                    connection.commit()
                    st.success('Inserted')


def _update():
    with st.form('Update'):
        table_name = st.selectbox('Table name:', [i[0] for i in run_query('SHOW TABLES;')])
        column_name = st.selectbox('Set Column:', table_col_names(table_name))
        value = st.text_input('With the Value:')
        condition = st.text_input('Where Condition are:')
        if st.form_submit_button('Submit'):
            run_query(f"""
                    UPDATE {table_name}
                    SET {column_name} = N'{value}'
                    WHERE {condition};
                    """)
            connection.commit()
            st.success('Updated')


def _delete():
    with st.form('Delete'):
        table_name = st.selectbox('Table name:', [i[0] for i in run_query('SHOW TABLES;')])
        condition = st.text_input('Condition:')
        if st.form_submit_button('Submit'):
            run_query(f"""
                    DELETE FROM {table_name}
                    WHERE {condition}
                    """)
            connection.commit()
            st.success('Deleted')


@st.experimental_singleton
def powered_by():
    st.info("""
    Student management using Python's module [Streamlit](https://streamlit.io/) and
     [MySQL](https://www.mysql.com/) hosted on [Free SQL database](https://www.freesqldatabase.com/).\n
    The emojis you've seen is available from
    [Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/).
    """)


if __name__ == '__main__':
    st.title('Data')
    menu()
    powered_by()
