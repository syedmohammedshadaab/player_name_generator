import streamlit as st
import cricketer
st.title("Player Nickname Generator")

player=st.sidebar.selectbox("Pick a Player_Name",("Virat Kholi","Ab De Villiers","mohammed siraj","chris gayle"))
if player:
    response=cricketer.crickter(player)
    st.header(response["city"].strip())
    st.write(response["tourist"].strip())