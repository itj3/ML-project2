# Module containing functions related to our temperature model
# Function names included here for control-f
# update_heat(...) - updates the temperature of a given room, as per equation provided.
# get_capacitance(...) - calculates the capacitance, derived from the equation provided.
# get_resistance(...) - calculates the resistance, derived from the equation provided.
# is_stable(...) - determines whether or not the model is stable according to delta < capacitance * resitance

def update_heat(delta_t, cap, res, inside_temp, outside_temp, flow_in):
    """
    updates the temperature of a given room, as per equation provided
    @param delta_t: the time interval or time step for updating heat
    @param cap: The capacitance of a room (Ch in equation)
    @param res: The resistance between a room and the environment (Rhe in equation)
    @param inside_temp: The temperature inside the room at time t (Th(t) in equation)
    @param outside_temp: The outside temperature at time t (Te(t) in equation)
    @param flow_in: The heat flow into the room from a heat source (qh(t) in equation)
    @return: the updated heat of the room (Th(t + delta) in equation)
    """

    return inside_temp + (delta_t / cap) * (flow_in - (inside_temp - outside_temp) / res)

def get_capacitance(delta_t, delta_heat, res, inside_temp, outside_temp, flow_in):
    """
    Calculates the capacitance, derived from the equation provided
    @param delta_t: the time interval or time step for updating heat
    @param delta_heat: the change of heat measured in delta_t (Th(t + delta) in equation)
    @param res: The resistance between a room and the environment (Rhe in equation)
    @param inside_temp: The temperature inside the room at time t (Th(t) in equation)
    @param outside_temp: The outside temperature at time t (Te(t) in equation)
    @param flow_in: The heat flow into the room from a heat source (qh(t) in equation)
    @return: the capacitance of the room (Ch in equation)
    """
    return (delta_t * (flow_in - (inside_temp - outside_temp) / res)) / (delta_heat - inside_temp)

def get_resistance(delta_t, delta_heat, cap, inside_temp, outside_temp, flow_in):
    """
    Calculates the resistance, derived from the equation provided
    @param delta_t: the time interval or time step for updating heat
    @param delta_heat: the change of heat measured in delta_t (Th(t + delta) in equation)
    @param cap: The capacitance of a room (Ch in equation)
    @param inside_temp: The temperature inside the room at time t (Th(t) in equation)
    @param outside_temp: The outside temperature at time t (Te(t) in equation)
    @param flow_in: The heat flow into the room from a heat source (qh(t) in equation)
    @return: the resistance of the room (Rhe in equation)
    """
    return -(inside_temp - outside_temp) / ((cap / delta_t * (delta_heat - inside_temp)) - flow_in)

def is_stable(delta_t, cap, res):
    """
    determines whether or not the model is stable according to delta < capacitance * resitance
    @param delta_t: the time interval or time step for updating heat
    @param cap: the capacitance of a room (Ch in equation)
    @param res: the resistance of a room (Rhe in equations)
    @return: boolean representing whether or not the model is stable
    """
    return delta_t < (cap * res)

