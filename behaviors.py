import sys
sys.path.insert(0, '../')
from planet_wars import issue_order
from random import choice

def spread_to_weakest_neutral_planet(state):

    strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)
    index = 0
    close_planetlist = sorted(state.neutral_planets(), key=lambda p: p.num_ships)
    close_planet = close_planetlist[index]
    my_planets = iter(sorted(state.my_planets(), key=lambda p: p.num_ships/p.growth_rate,reverse=True))
    neutral_planets = iter(sorted(state.neutral_planets(), key=lambda p: p.num_ships/p.growth_rate))
    close_planet = next(neutral_planets)
    
    try:
        for fleet in state.my_fleets():
            if fleet.destination_planet == close_planet.ID and index +1 < len(close_planetlist):
                close_planet = next(neutral_planets)
    except StopIteration:
        return

    if not close_planet or not strongest_planet or close_planet.num_ships + 1 > strongest_planet.num_ships:
        return False
    return issue_order(state, strongest_planet.ID, close_planet.ID, close_planet.num_ships + 1)
		
			
def start_spread(state):        
    strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)
    weakest_planet = min(state.enemy_planets(), key=lambda p: p.num_ships/p.growth_rate, default=None)
    if strongest_planet and weakest_planet and strongest_planet.num_ships <weakest_planet.num_ships +20:
        return False
    return issue_order(state, strongest_planet.ID, weakest_planet.ID, weakest_planet.num_ships+(weakest_planet.growth_rate * state.distance(weakest_planet.ID,strongest_planet.ID))+2)
    
def defense_action(state):
    my_planets = iter(sorted(state.my_planets(), key=lambda p: p.num_ships,reverse=True))
    our_planet = next(my_planets)
    my_list = state.my_planets()
    for enemy in state.enemy_fleets():
        for my in my_list:
            if enemy.destination_planet == my.ID:
                need = enemy.num_ships - my.num_ships
                if need < our_planet.num_ships and our_planet.num_ships > 3:
                    issue_order(state,our_planet.ID,enemy.destination_planet,3)
                
    return
            
    
