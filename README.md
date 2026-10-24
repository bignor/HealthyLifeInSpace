# HealthyLifeInSpace
# HABITAT HERO — TEAM TODO LIST
# Goal: Keep 4 astronauts supplied for 7 simulated days.

# PERSON 1: GAME LOGIC
# Branch: game-logic | File: game_logic.py

# TODO 3: Choose starting oxygen, water, and power amounts.
# Define units and maximum storage.
# Work with Person 3 to label simplified assumptions.

# TODO 8: Calculate one day's resource changes.
# Add solar power without exceeding battery capacity.
# Run equipment only when enough inputs are available.
# The oxygen generator uses power and water.
# The recycler recovers part of the crew's used water.
# Subtract daily crew consumption and essential power use.

# TODO 9: Prevent impossible resource values.
# Track unmet needs before limiting resources to zero.
# Keep resources within their storage limits.

# TODO 10: Create the dust-storm event.
# Reduce solar power for a clearly defined duration.
# Give the player a warning before advancing.

# TODO 11: Calculate the resource forecast.
# Estimate which supply will run out first.
# Assume the current equipment settings continue.

# TODO 12: Check for success or failure after each day.
# Fail if an essential need cannot be met.
# Win after completing all 7 days.

# TODO 13: Return a result explaining why the mission ended.


# PERSON 2: GAME SCREEN
# Branch: game-screen | File: app.py

# TODO 1: Import Streamlit and Person 1's game functions.

# TODO 2: Add the title, mission goal, and instructions.

# TODO 4: Store progress in st.session_state.
# Save the day, resources, equipment settings, storm, and result.

# TODO 5: Display the current day and resource amounts.
# Add oxygen, water, and power progress bars with units.

# TODO 6: Add switches for the generator and recycler.
# Explain each system's resource costs.

# TODO 7: Add the "Next Day" button.
# Connect it to Person 1's daily calculations.
# Each click advances exactly one day.
# Display storm warnings, forecasts, and result messages.
# Disable game actions after the mission ends.

# TODO 14: Add a "Restart Mission" button.
# Reset all progress and equipment settings.

# TODO 16: Improve colors, spacing, and warning messages.


# PERSON 3: SCIENCE, TESTING, AND PRESENTATION
# Branch: science-testing | Files: science.py, test_notes.md

# TODO 15: Research and add NASA sources.
# Explain water recycling, oxygen generation, and solar power.
# Help Person 1 choose and document simulation assumptions.
# Write the science section for Person 2 to display.

# TODO 17: Test the combined game.
# Test a successful mission and a failed mission.
# Test the storm and insufficient equipment inputs.
# Check that each click advances only one day.
# Check that restarting resets everything.
# Record problems in test_notes.md for the team to fix.

# TODO 18: Prepare the presentation with the whole team.
# Explain the goal, science, choices, and calculations.
# Practice a short demo that includes the dust storm.


# EVERYONE: COMBINE YOUR WORK IN THE main BRANCH
# Agree on function names and inputs before working separately.
# Get a basic version working together first.
# Combine finished changes regularly and check the game runs.
# Make sure everyone can explain the finished program.