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

#Progress of days
DAYS = [ "Sunday", "Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday"]

# Tracking the variable 
if "days_progress" not in st.session_state:
    st.session_state.days_progress = 0 #Starting from sunday

RESOURCES = ["Water", "Power", "Oxygen"]

if "water" not in st.session_state:
    st.session_state.water = 10

if "power" not in st.session_state:
    st.session_state.power = 10

if "oxygen" not in st.session_state:
    st.session_state.oxygen = 10

option = st.selectbox("What is your resource?", RESOURCES, key="my_choice")

st.write(f"You selected: {st.session_state.my_choice}")

#tracking dust storm
if "storm" not in st.session_state:
    st.session_state.storm = 1

if "result" not in st.session_state:
    st.session_state.result = False


#this displays the day and what is stored in that value
st.write(DAYS[st.session_state.days_progress])

# displaying the amount of usuage
st.write("Resource Amounts")

#progress shows us the bar resource level
#metric gives the number amount that is left
progress_text = "Water Remaining"
st.metric(label="Water Remaining", value = st.session_state.water)
my_bar = st.progress(st.session_state.water * 10, text=progress_text)


progress_text = "Power Remaining"
st.metric(label= "Power Remaning", value = st.session_state.power)
my_bar = st.progress(st.session_state.power * 10, text=progress_text)

progress_text = "Oxygen Remaining"
st.metric(label= "Oxygen Remaining", value = st.session_state.oxygen)
my_bar = st.progress(st.session_state.oxygen * 10, text=progress_text)


#toggle stores true or false its our switch
st.toggle(label="Oxygen Generator", key= "generator_on")

st.toggle(label="Water Recycler", key="recycler_on")

st.subheader("Generator Rules")
st.write("Oxygen Generator: Produces 10 kg of oxygen per day using 20 liters of water and 30 kWh of power")
st.write("Water Recycler: This recovers 5 liters of water per day")











