import streamlit as st
#from game_logic import start_game_logic


#Display messages
st.title("Open Doors To The New World")
st.subheader("The Mission")
st.write("The goal is to keep 4 astronauts alive on mars for a maximun of 7 days." \
" You have resources such as oxygen, power, and water as your help. " \
"Your obstacle will be to avoid running out of supllies by the end of the day while facing a dust storm.")

st.divider()

st.subheader("How to play")
st.write("Choose only 1 resource per day.")
st.write("You can't choose the same resource two days in a row.")
st.write("The emergency supplies uses up your resources leaving you with less for the next days.")
st.write("Watch your resource bars they will show the length of what you have left")

#Setting up the days to choose from
#if "day_progress" not in st.session_state:

