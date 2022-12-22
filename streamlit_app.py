# streamlit_app.py
import mysql.connector
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu as om


def init_connection():
    return mysql.connector.connect(**st.secrets["mysql"])


connection = init_connection()


def run_query(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()


# Function that returns the table's column names
def col_names(table_name):
    return [row[0] for row in run_query(f"SHOW COLUMNS FROM {table_name};")]


def table_names():
    return [i[0] for i in run_query('SHOW TABLES;')]


def example():
    with st.echo():  # Displays the codes and then executes it
        st.write('Some queries :mag:')

        # Function returns tables read from the database with provided table names
        def examples(table_name):
            return pd.DataFrame(
                run_query(f'SELECT * FROM {table_name};'),
                columns=col_names(table_name)
            )

        for table in table_names():
            st.header(f'Table {table}')
            st.write(examples(table))


def menu():
    example()

    # Adapt names with its choices
    def _choices(ch, ops):
        for option in ops:
            if ch == option:
                _query = eval(f"_{option.lower()}()")  # For instance: _update()
                if st.button(option):
                    run_query(_query)
                    st.success(f'{option} successfully')
                    connection.commit()  # Essentially statement

    column1, column2 = st.columns([0.6, 0.4])
    with column1:
        # Query directly from the web
        the_query = st.text_area('The query:', 'SELECT * FROM Pets;')
        if st.button('Query'):
            st.write(pd.DataFrame(run_query(the_query)))
    with column2:
        options = ['Insert', 'Update', 'Delete']
        choice = om(None, options)
        _choices(choice, options)


def _insert():
    table_name = st.selectbox('Table name:', table_names())

    student_id = st.number_input('StudentID:')  # 8 eight attributes
    student_name = st.text_input('Name:')
    major = st.text_input('Major:')
    dob = st.date_input('DOB:')
    learning_course = st.date_input('Course:').year
    fees = st.number_input('Remaining fees:')
    dormitory = st.radio('In dormitory?', ['No', 'Yes'])
    address = st.text_area('Address')

    return f"""
            INSERT INTO
                {table_name}
            VALUES
                ('{student_id}', '{student_name}', '{major}', '{dob}',
                '{learning_course}', '{fees}', '{dormitory}', '{address}');
            """


def _update():
    table_name = st.selectbox('Table name:', [i[0] for i in run_query('SHOW TABLES;')])
    column_name = st.selectbox('Set Column:', col_names(table_name))
    value = st.text_input('With the Value:')
    condition = st.text_input('Where Condition are:')
    return f"""
            UPDATE {table_name}
            SET {column_name} = N'{value}'
            WHERE {condition};
            """


def _delete():
    table_name = st.selectbox('Table name:', [i[0] for i in run_query('SHOW TABLES;')])
    condition = st.text_input('Condition:')
    return f"""
            DELETE FROM {table_name}
            WHERE {condition}
            """


if __name__ == '__main__':
    st.title('Data')
    col1, col2 = st.columns(2)
    with col1:
        st.info("""
                    Student management using Python's module [Streamlit](https://streamlit.io/)
                      and
                     [MySQL](https://www.mysql.com/) hosted on [Free SQL database](https://www.freesqldatabase.com/)
                     """)
    with col2:
        st.info("""
                    The emojis you've seen is available from
                    [Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
                    """)
    menu()
