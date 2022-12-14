import streamlit as st


def boo(prompt):
    v = st.text_input(prompt)
    return v == 'y'


def num(prompt):
    v = st.text_input(prompt)
    if v.isnumeric():
        return v


def cha(prompt, variant):
    import string
    
    v = st.text_input(prompt)

    acquiesced = ''
    if variant == 'name':
        acquiesced = f' {string.ascii_letters}'
    elif variant == 'no_space':
        acquiesced = f'{string.ascii_letters}{string.digits}{string.punctuation}'
    elif variant == 'date':
        acquiesced = f'-{string.digits}'

    if {*v}.issubset({*acquiesced}):  # unpacking the string to items in the set
        return v
