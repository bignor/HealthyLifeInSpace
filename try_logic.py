from game_logic import new_game, simulate_day, get_warning, storm_active, forecast, check_result

#test 1: generator on
state = new_game()
result = simulate_day(state)
print("Encendido: ", result)

#Test 2: generator off
state = new_game()
state["generator_on"] = False
result = simulate_day(state)
print("Apagado: ", result)

state = new_game()
state["oxygen"] = 1
state["generator_on"] = False
new_state, report = simulate_day(state)
print("Oxygen generator on with low oxygen: ", new_state["oxygen"], report)

for day in range(1, 8):
    state = new_game()
    state["day"] = day
    print(day, get_warning(state))

state = new_game()
state["generator_on"] = False
state["day"] = 3
new_state, report = simulate_day(state)
print("Dust storm day 3: ", new_state["power"])

state = new_game()
state["oxygen"] = 5
state["generator_on"] = False
print("Forecast without generator: ", forecast(state))

print ("Normal Forecast: ", forecast(new_game()))

state = new_game()
state["oxygen"] = 1
state["generator_on"] = False
new_state, report = simulate_day(state)
print(check_result(new_state, report))

state = new_game()
state["generator_on"] = False
while True:
    state, report = simulate_day(state)
    result = check_result(state, report)
    print(state["day"], result)
    if result["status"] != "playing":
        break

print("--- Combinaciones de interruptores ---")
for gen in (True, False):
    for rec in (True, False):
        state = new_game()
        state["generator_on"] = gen
        state["recycler_on"] = rec
        print("generador", gen, "| reciclador", rec, "->", forecast(state))

print("--- Generador solo 2 días ---")
state = new_game()
while True:
    state["generator_on"] = state["day"] <= 2
    state, report = simulate_day(state)
    result = check_result(state, report)
    if result["status"] != "playing":
        print(result)
        break
