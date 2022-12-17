import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu as om

import mysql.connector
import pandas as pd
import numpy as np
import datetime

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


@st.experimental_singleton
def example():
    st.markdown("A connection test with MySQL remote server")
    
    # Displays the codes and then executes it
    with st.echo():
        st.write('Some queries examples')
        # Function that returns the table's column names
        col_names = lambda table_name: [column[0] for column in run_query(f"SHOW COLUMNS FROM {table_name};")]
        
        # Function returns tables read from the database with provided table names
        examples = lambda table_name: pd.DataFrame(run_query( f'SELECT * FROM {table_name};' ), columns=col_names(table_name))
        for i in ['Pets', 'Student']:
            st.write(examples(i))
                 
    # Horizontal line separator
    components.html("""<hr style="height:1px;
                    border:none;
                    color:#333;
                    background-color:#333;" 
                    /> """)


def menu():
    col1, col2 = st.columns(2)
    with col1:
        choice = om('Main menu', ['Insert'])
        
        # Query directly from the web
        the_query = st.text_area('The query:')
        if st.button('Query'):
            st.write(pd.DataFrame( run_query(the_query) ))
    with col2:
        if choice == 'Insert':
            with st.expander('Infos'):
                table_name = st.text_input('Table name:')
                st.markdown('---')
                user_input = [
                    st.number_input('StudentID:'),
                    st.text_input('Name:'),
                    st.text_input('Major:'),
                    st.date_input('DOB:'),
                    st.date_input('Course:').year,
                    st.number_input('Remaining fees:'),
                    st.radio('In dormitory?', ['No', 'Yes']),
                    st.text_area('Address'),
                ]
            if st.button('Commit'):
                st.write(user_input)
                # run_query(f"""
                #         INSERT INTO {table_name} VALUES(
                #         {np.array_split(user_input, 8)}
                #         )
                #         """)
    


if __name__ == '__main__':
    st.snow()
    example()
    menu()
