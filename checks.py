

def if_neutral_planet_available(state):
    return any(state.neutral_planets())

            
def spread_check(state):
    weakest_planet = min(state.enemy_planets(), key=lambda p: p.num_ships, default=None)
    strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)
    if weakest_planet and strongest_planet:
        return True
        
def defense_check(state):
    return any(state.enemy_fleets())