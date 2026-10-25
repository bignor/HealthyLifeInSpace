import streamlit as st
from game_logic import new_game, simulate_day, get_warning, storm_active, forecast, check_result

#better layout
st.set_page_config(layout="wide")

if "mission_started" not in st.session_state:
    st.session_state.mission_started = False
if not st.session_state.mission_started: 
    st.title("🚀 Healthy Life in Space?")
    st.subheader("Can you keep the crew and station healthy?") 
    st.write("Manage water, oxygen, and power to complete your mission.")


    if st.button("Start mission"):
        st.session_state.mission_started = True 
        st.rerun()
    st.stop()
    

#Display messages
st.title("Open Doors To The New World")
st.subheader("The Mission")
st.write("The goal is to keep 4 astronauts alive on mars for a maximun of 7 days." \
" You have resources such as oxygen, power, and water as your help. " \
"Your obstacle will be to avoid running out of supllies by the end of the day while facing a dust storm.")

st.divider()

#allowing you to open and close the instructions
with st.expander("📖 How to play"):

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

# displaying the amount of usuage
if "game_state" not in st.session_state:
    st.session_state.game_state = new_game()

#this displays the day current day and whats stored in DAYS
if st.session_state.game_state["day"] <= 7:
    st.subheader(DAYS[st.session_state.game_state["day"] - 1])

#saving the starting game


if "result" not in st.session_state or isinstance(st.session_state.result, bool):
    st.session_state.result = {
        "status": "playing",
        "reason": "Mission ongoing." 
    }

    

#this divides the on side for the crew and then for the resources
crew_column, resource_column = st.columns(2)

with crew_column:
    st.subheader("Your Crew")
    st.write("Keep all 4 astronauts alive for 7 days.")
    st.image("astronauts.png")


    #disabling the next day if the saved status is not playing
    if st.button("Next Day", type="primary", 
                 disabled= st.session_state.result["status"] != "playing"):

        #sending the players choices into the calculations
        st.session_state.game_state["generator_on"] = st.session_state.generator_on
        st.session_state.game_state["recycler_on"] = st.session_state.recycler_on


        #taking my current game and caulating the day
        new_state, report = simulate_day(st.session_state.game_state)

        st.session_state.game_state = new_state #saving the progress


        #checking to see if you won, lost, or still playing the game
        st.session_state.result = check_result(st.session_state.game_state, report)
        

        st.rerun()


    

with resource_column:
    st.write("Resource Amounts")

#progress shows us the bar resource level
#metric gives the number amount that is left

    st.subheader("💧 Water Remaining")
    st.metric(label="Water Remaining (liters)", value=f'{st.session_state.game_state["water"]:.0f}')
    my_bar = st.progress(st.session_state.game_state["water"] / 60,)

    st.subheader("🪫 Power Remaning")
    st.metric(label= "Power Remaning", value = f'{st.session_state.game_state["power"]:.0f}')
    my_bar = st.progress(st.session_state.game_state["power"] / 180,)

    st.subheader("💨 Oxygen remaining")
    st.metric(label= "Oxygen Remaining", value = f'{st.session_state.game_state["oxygen"]:.0f}')
    my_bar = st.progress(st.session_state.game_state["oxygen"] / 12,)


    #toggle stores true or false its our switch
    st.toggle(label="Oxygen Generator", key= "generator_on")

    st.toggle(label="Water Recycler", key="recycler_on")

    st.subheader("Generator Rules")
    st.write("Oxygen Generator: Produces 10 kg of oxygen per day using 20 liters of water and 30 kWh of power")
    st.write("Water Recycler: This recovers 5 liters of water per day")


#showing how the mission ended
if st.session_state.result["status"] == "lose":
    st.error(st.session_state.result["reason"])
elif st.session_state.result["status"] == "win":
    st.success(st.session_state.result["reason"])
    st.balloons()



st.subheader("Storm Warning")

#storing the messsage for current game
warning_state = get_warning(st.session_state.game_state)
#displaying if it happends
if warning_state:
    st.warning(warning_state)

st.subheader("Forecast")
forecast_state = forecast(st.session_state.game_state)

#displaying if it happends
if forecast_state["resource"] is not None:
    st.write(f"Resource at risk: {forecast_state['resource']}. Predicted day: {forecast_state['day']}. ")
else:
    st.write("Forecase: Supplies should last through the mission with the current equipment setting.")


def reset_state():
    st.session_state.game_state = new_game()
    st.session_state.result = {"status": "playing", "reason": "Mission ongoing."}
    st.session_state.generator_on = st.session_state.game_state["generator_on"]
    st.session_state.recycler_on = st.session_state.game_state["recycler_on"]
    

st.button("Reset Mission", on_click=reset_state)





