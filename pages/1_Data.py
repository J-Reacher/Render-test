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


def main():
    col_names = lambda table_name: [column[0] for column in run_query(f"SHOW COLUMNS FROM {table_name};")]

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
