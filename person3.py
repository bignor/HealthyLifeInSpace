import streamlit as st  # Imports Streamlit with the short name "st" for use in this app.



print("The three most imporantt thing with the resource of water is knowing what machine does what")
print("Urine machine take pee and separtes air from liquid, while its gets spun and heated to remove the water from the urine, leaving behind a dry waste.")
print("Air machine is running 24/7 and is used to pull all the breths and sweat moisture right out of the air")
print("Cleaner machine holds all the dirty water in one tank. A chemical filter for salts and smells, a hot reactor that burns up any germs, soap, or leftovers, and final filter so it tastes normal")




print("You get the oxygen from the air you can breathe, out of water")
print("But in a sealed capsule, CO2 can become deadly if you don't remove it under 24 hours")
print("You use the OGS(Oxygen Generation System) which is water + electricity to make oxygen and hydrogen")
print("From the water recycling system it will split the H20 into O2 and H2. Oxygen goes straight to the cabin while H2 is either vented into space or sent to another system to make more water")


print("Unlike on earth where the sunlight can be block by the earth in space you have unlimted access to the sunlight")
print("The solar panels are used to power the station and the water recycling system")
print("Only form of energy that can be used in space is sunlight, so the solar panels are very important to the station")
print("The solar panels can convert sunlight into electricity, which is then used to power all the systems on the station,")



print("If you open a hatch, air will rush out because gas will always move from high pressure to low pressure")
print("Lungs care about oxygen molecules hit per breath, if you get to little pressure then you won't be able to get oxygen in your blood")
print("Everything needs to ne energy transfer")
print("You lose 2.5L per day thorugh pee, swear, and breathing")
print("breathe in 0.8kg of O2 per day to burn food for energy")
print("you breathe out 1kg of CO2 per day as waste")
print("Make about 100 watts of heat just by existing")



st.write("👩‍🚀")  # Shows an astronaut emoji as a simple placeholder image in the Streamlit app.

st.header("Astronaut Alex")  # Displays the astronaut's name as a heading in the app.
st.write("Hello, space explorer! I'm ready to keep the station healthy!")  # Greets the player in the Streamlit app.

situation_messages = {  # Stores a display message for each possible game situation.
	"normal supplies": "Supplies are stable. Keep monitoring water, oxygen, and power.",
	"low supplies": "Supplies are running low. Conserve resources and check the station systems.",
	"dust storm": "A dust storm is reducing solar power. Save energy until sunlight returns.",
	"winning": "Mission success! The crew kept the station healthy.",
	"losing": "Mission failed. Review your resource choices and try again.",
}  # The game can look up the matching text using a situation name.

def show_situation(situation):  # Defines the display function; use this name and situation keys when connecting Person 2's game logic.
	normalized_situation = situation.strip().lower()  # Makes matching work regardless of capitalization or extra spaces.
	message = situation_messages.get(normalized_situation, "Unknown situation. Check the situation name.")  # Gets the matching text, or a helpful fallback.
	st.write("👩‍🚀")  # Displays the astronaut for the current situation.
	st.info(message)  # Displays the message that matches the situation.

for test_situation in situation_messages:  # Tries the display function once for every situation key before game logic is connected.
	show_situation(test_situation)  # Shows the astronaut and message so you can check each test in the app.

def update_display_from_game(current_situation):  # Accepts the situation that Person 1's game rules determine.
	show_situation(current_situation)  # Sends that game result to the astronaut display; Person 2 can call this after updating the game.

# TODO 8: Add the science explanations and NASA source links.
# Clearly label simplified game assumptions.

