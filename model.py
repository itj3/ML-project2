# Module containing functions related to our temperature model
# Function names included here for control-f
# update_heat(...) - updates the temperature of a given room, as per equation provided.
# get_capacitance(...) - calculates the capacitance, derived from the equation provided.
# get_resistance(...) - calculates the resistance, derived from the equation provided.
# is_stable(...) - determines whether or not the model is stable according to delta < capacitance * resistance


def update_heat(delta_t, tau, epsilon, inside_temp, outside_temp):
    """
    updates the temperature of a given room, as per equation provided
    @param delta_t: the time interval or time step for updating heat
    @param tau: product of capacitance and epsilon
    @param epsilon: Margin of error
    @param inside_temp: The temperature inside the room at time t (Th(t) in equation)
    @param outside_temp: The outside temperature at time t (Te(t) in equation)
    @return: the updated heat of the room (Th(t + delta) in equation)
    """

    return inside_temp + epsilon + (delta_t * -(inside_temp - outside_temp)) / tau


def get_tau(delta_t, delta_heat, inside_temp, outside_temp):
    """
    Calculates tau - the produce of the capacitance and the resistance
    @param delta_t: the time interval or time step for updating heat
    @param delta_heat: the change of heat measured in delta_t (Th(t + delta) in equation)
    @param inside_temp: The temperature inside the room at time t (Th(t) in equation)
    @param outside_temp: The outside temperature at time t (Te(t) in equation)
    @return: tau
    """
    return -(delta_t * (inside_temp - outside_temp)) / (delta_heat - inside_temp)


def is_stable(delta_t, cap, res):
    """
    determines whether or not the model is stable according to delta < capacitance * resitance
    @param delta_t: the time interval or time step for updating heat
    @param cap: the capacitance of a room (Ch in equation)
    @param res: the resistance of a room (Rhe in equations)
    @return: boolean representing whether or not the model is stable
    """
    return delta_t < (cap * res)


def infer_vars(room):
    """
    Uses data from the rooms to infer tau and epsilon for the whole data set
    @param room: a room object containing temps and timestamps
    @return the tuple containing the final tau and epsilon for the data set
    """
    # dt is determined to be 10 from data
    # we could calculate this from the data, but there are some weird timestamps that throw off calculations.
    dt = 10
    # list to store all calculated capacitance for a particular room
    all_tau = []
    for i in range(len(room.temps) - 1):
        all_tau.append(get_tau(
            dt,
            room.temps[i + 1][1] - room.temps[i][1],
            room.temps[i][1],
            room.temps[i][2]
        ))

    # check to make sure the node actually had readings
    if all_tau:
        # calculate the mean tau
        tau = sum(all_tau) / len(all_tau)
        # epsilon is the difference between dt and tau. add .5 to consider stability condition
        return tau, abs(dt - tau) + .5
    else:
        return None

def all_tau(room):
    dt = 10
    # list to store all calculated capacitance for a particular room
    all_tau = []
    time = []
    dates = []

    for i in range(len(room.temps) - 1):
        all_tau.append(get_tau(
            dt,
            room.temps[i + 1][1] - room.temps[i][1],
            room.temps[i][1],
            room.temps[i][2]
        ))
        dates.append(room.temps[i][0])

    return  [all_tau,dates]

