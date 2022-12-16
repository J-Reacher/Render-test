import streamlit as st
from streamlit_option_menu import option_menu as om
import mysql.connector

from utils import Template
data = Template('Data')


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
            int(st.number_input('ID: ')),
            st.text_input('Name: '),
            st.text_input('Major: '),
            st.date_input('Date of birth (yyyy-mm-dd): '),
        ]
    with col2:
        column2 = [
            st.text_input('Course (yyyy-yyyy): '),
            st.number_input('Remaining tuition fee: vnd'),
            st.checkbox('In the dormitory '),
            st.text_area('Address: '),
        ]
    return column1 + column2


if __name__ == '__main__':
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
                    Student management using [MySQL](https://www.mysql.com/)
                    and Python's module [Streamlit](https://streamlit.io/)
                    """)
    with col2:
        st.markdown("""
                    
                    """)
    with col3:
        run_query('SELECT * FROM Pets')

    choice = om(None, ['Insert', 'Drop', 'Alter'],
                default_index=0, orientation='horizontal')
    
    # run_query("""
    #    CREATE TABLE Student (
    #        Name VARCHAR(64),
    #        Major VARCHAR(32),
    #        DOB DATE,
    #        Course YEAR,
    #        Remaining_fee FLOAT(10),
    #        In_dormitory ENUM('y', 'n'),
    #        Address VARCHAR(128),
    #        studentID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    #        PRIMARY KEY (studentID)
    #    );
    # """)
    
    if choice == 'Insert':
        rows = run_query('SELECT * FROM Pets;')
        for row in rows:
            st.write(f"{row[0]} has a :{row[1]}:")
            
        # run_query('SELECT * FROM Student;')
