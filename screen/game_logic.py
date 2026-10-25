# HealthyLifeInSpace
# HABITAT HERO — TEAM TODO LIST
# Goal: Keep 4 astronauts supplied for 7 simulated days.

# PERSON 1: GAME LOGIC
# Branch: game-logic | File: game_logic.py

# TODO 3: Choose starting oxygen, water, and power amounts.
# Define units and maximum storage.
# Work with Person 3 to label simplified assumptions.

CREW = 4
DAYS = 7

#unit definitions Oxygen: kg, Water: liters, Power: kWh
MAX_STORAGE = {"oxygen": 100.00, "water": 200.00, "power": 500.00}
INITIAL_STORAGE = {"oxygen": 10.00, "water": 100.00, "power": 250.00}

OXYGEN_PER_CREW_PER_DAY = 0.50  # kg per crew member per day
WATER_PER_CREW_PER_DAY = 2.00  # liters per crew member per day
POWER_PER_CREW_PER_DAY = 13.00  # kWh per crew member per day
SOLAR_PANEL_OUTPUT_PER_DAY = 50.00  # kWh per day

GEN_OXYGEN = 10.00  # kg per day the generator produces per day
GEN_WATER = 20.00  # liters per day the generator consumes per day
GEN_POWER = 30.00  # kWh per day the generator consumes per day

RECYCLER_WATER = 5.00 # liters per day the recycler recovers per day
DUST_STORM_POWER_LOSS = 20.00 # kWh per day lost during a dust storm

DUST_STORM_START = 3        #start on day 3
DUST_STORM_DURATION = 4     #how many days the dust storm lasts


def new_game():
    return {
        "day": 1,
        "oxygen": INITIAL_STORAGE["oxygen"],
        "water": INITIAL_STORAGE["water"],
        "power": INITIAL_STORAGE["power"],
        "generator_on": True,
        "recycler_on": True,
    }


# TODO: Create the dust-storm event.
# Reduce solar power for a clearly defined duration.
# Give the player a warning before advancing.
def storm_active(day):
    return DUST_STORM_START <= day < DUST_STORM_START + DUST_STORM_DURATION

def get_warning(state):
    day = state["day"]
    if day == DUST_STORM_START - 1:
        return "Warning: Dust storm expected tomorrow."
    if storm_active(day):
        return "Warning: There is a dust storm."
    return None


# TODO: Calculate one day's resource changes.
# Add solar power without exceeding battery capacity.
# Run equipment only when enough inputs are available.
# The oxygen generator uses power and water.
# The recycler recovers part of the crew's used water.
# Subtract daily crew consumption and essential power use.
def simulate_day(state):
    oxygen = state["oxygen"]
    water = state["water"]
    power = state["power"]
    generator_on = state["generator_on"]
    recycler_on = state["recycler_on"]

    # Add solar power
    solar = SOLAR_PANEL_OUTPUT_PER_DAY
    if storm_active(state["day"]):
        solar = solar - DUST_STORM_POWER_LOSS
    power = min(power + solar, MAX_STORAGE["power"])


    # OXYGEN GENERATOR
    if generator_on and power >= GEN_POWER and water >= GEN_WATER:
        oxygen = oxygen + GEN_OXYGEN
        water = water - GEN_WATER
        power = power - GEN_POWER
        

    # Water Recycler
    if recycler_on:
        water = water + RECYCLER_WATER
        water = min(water, MAX_STORAGE["water"])
    

    # Calculate daily consumption
    oxygen = oxygen - (OXYGEN_PER_CREW_PER_DAY * CREW)
    water = water - (WATER_PER_CREW_PER_DAY * CREW)
    power = power - (POWER_PER_CREW_PER_DAY * CREW)

    # TODO 9: Prevent impossible resource values.
    # Track unmet needs before limiting resources to zero.
    unmet = {
        "oxygen": max(0, -oxygen),
        "water": max(0, -water),
        "power": max(0, -power),
    }

    # Keep resources within their storage limits.
    oxygen = max(0, min(oxygen, MAX_STORAGE["oxygen"]))
    water = max(0, min(water, MAX_STORAGE["water"]))
    power = max(0, min(power, MAX_STORAGE["power"]))


    new_state = { 
        "day": state["day"] + 1,
        "oxygen": oxygen,
        "water": water,
        "power": power,
        "generator_on": generator_on,
        "recycler_on": recycler_on,
    }
    report = {"unmet": unmet}
    return new_state, report


# TODO 11: Calculate the resource forecast.
# Estimate which supply will run out first.
# Assume the current equipment settings continue.
def forecast(state):
    sim = state
    while sim["day"] <= DAYS:
        day = sim["day"]
        sim, report = simulate_day(sim)
        for resource, missing in report["unmet"].items():
            if missing > 0:
                return {"resource": resource, "day": day}
    return {"resource": None, "day": None}


# TODO 12: Check for success or failure after each day.
# Fail if an essential need cannot be met.
# Win after completing all 7 days.
def check_result(state, report):
    for resource, missing in report["unmet"].items():
        if missing > 0:
            
            # TODO 13: Return a result explaining why the mission ended.
            return {
                "status": "lose",
                "reason": f"Mission failed: the {resource} supply ran out on day {state['day'] - 1}.",
            }
    
    if state["day"] > DAYS:
        return {
            "status": "win",
            "reason": "Mission successful: all 7 days completed with sufficient resources.",
        }
        
    return {
        "status": "playing",
        "reason": "Mission ongoing: resources are sufficient for now.",
    }











