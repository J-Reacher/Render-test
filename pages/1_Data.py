import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu as om

import mysql.connector
import pandas as pd

from template import Template
data = Template('Data')

st.sidebar.info(("""
                    Student management using Python's module [Streamlit](https://streamlit.io/)
                    and
                    [MySQL](https://www.mysql.com/) hosted on [FreeSQLdatabase](https://www.freesqldatabase.com/)
                    """))
st.sidebar.info("""
                The emojis you've seen is available from [Streamlit emoji shortcodes](https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/)
                """)


def sep():
    # Horizontal line separator
    components.html("""<hr style="height:1px;
                    border:none;
                    color:#333;
                    background-color:#333;" 
                    /> """)


def execute():
    your_codes = st.text_area('Codes you type below will be executed directly:', "st.write(':sunny: Nam has a :snake: pet in his backyard')")
    if st.button('Execute'):
        eval(your_codes)


def example():
    # Displays the codes and then executes it
    with st.echo():
        st.write('Some queries examples')
        # Function that returns the table's column names
        col_names = lambda table_name: [column[0] for column in run_query(f"SHOW COLUMNS FROM {table_name};")]
        
        # Function returns tables read from the database with provided table names
        examples = lambda table_name: pd.DataFrame(run_query( f'SELECT * FROM {table_name};' ), columns=col_names(table_name))
        col1, col2 = st.columns([0.3, 0.7])  # Column1 will take 0.3 width and Column2 will take 0.7 width of the page
        with col1:
            st.header('Table Pets')
            st.write(examples('Pets'))
        with col2:
            st.header('Table Student')
            st.write(examples('Student'))


def menu():
    col1, col2 = st.columns([0.6, 0.4])
    with col1:
        # Query directly from the web
        the_query = st.text_area('The query:')
        if st.button('Query'):
            st.write(pd.DataFrame( run_query(the_query) ))
            
    with col2:
        choice = om('Main menu', ['Insert'])
        if choice == 'Insert':
            with st.expander('Insert infos'):
                st.markdown('---')
                # the_query = _extracted_from_menu()
            # if st.button('Commit'):
            #     run_query(the_query)


def _extracted_from_menu():
    table_name = st.selectbox('Table name:', [i[0] for i in run_query('SHOW TABLES;')])

    studentID = st.number_input('StudentID:')
    studentName = st.text_input('Name:')
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
                ('{studentID}', '{studentName}', '{major}', '{dob}', '{learning_course}', '{fees}', '{dormitory}', '{address}');
            """


if __name__ == '__main__':
    execute()
    sep()
    
    # Initialize connection.
    # Uses st.experimental_singleton to only run once.
    @st.experimental_singleton
    def init_connection():
        return mysql.connector.connect(**st.secrets["mysql"])

    conn = init_connection()

    # Perform query.
    # Uses st.experimental_memo to only rerun when the query changes or after 10 min.
    @st.experimental_memo(ttl=600)
    def run_query(query):
        with conn.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()
    
    st.markdown("A connection test with MySQL remote server")
    example()
    sep()
    
    menu()
