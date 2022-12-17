import streamlit as st
import streamlit.components.v1 as components

import mysql.connector
import pandas as pd

from utils import Template
data = Template('Data')

st.sidebar.info(("""
                    Student management using Python's module [Streamlit](https://streamlit.io/)
                    and
                    [MySQL](https://www.mysql.com/) hosted on [FreeSQLdatabase](https://www.freesqldatabase.com/)
                    """))

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


def get_input():
    col1, col2 = st.columns(2)
    with col1:
        column1 = [
            int(st.number_input('ID:')),
            st.text_input('Name:'),
            st.text_input('Major:'),
            st.date_input('Date of birth (yyyy-mm-dd):'),
        ]
    with col2:
        column2 = [
            st.text_input('Course (yyyy-yyyy):'),
            st.number_input('Remaining tuition fee: vnd'),
            st.checkbox('In the dormitory?'),
            st.text_area('Address:'),
        ]
    return column1 + column2


def main():
    def col_names(table_name):
        return [column[0] for column in run_query(f"SHOW COLUMNS FROM {table_name};")]

    st.markdown("A connection test with MySQL remote server")
    with st.echo():
        st.write('Some queries examples')
        st.write(pd.DataFrame(run_query('SELECT * FROM Pets;'),  columns=col_names('Pets')))
        st.write(pd.DataFrame(run_query('SELECT * FROM Student'),columns=col_names('Student')))
        
    components.html("""<hr style="height:1px;
                    border:none;
                    color:#333;
                    background-color:#333;" 
                    /> """)

    # the_table_name = st.text_input('Table name:')
    the_query = st.text_area('The query:')
    if st.button('Query'):
        st.write(pd.DataFrame( run_query(the_query) ))


if __name__ == '__main__':
    main()
