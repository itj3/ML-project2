# Module containing functions related to our temperature model
# Function names included here for control-f
# update_heat(...) - updates the temperature of a given room, as per equation provided.
# get_tau(...) - calculates tau, the product of capacitance and resistance
# clean_data(...) - removes tau values <= 0
# is_stable(...) - determines whether or not the model is stable according to delta < capacitance * resistance


def update_heat(delta_t, tau, inside_temp, outside_temp):
    """
    updates the temperature of a given room, as per equation provided
    @param delta_t: the time interval or time step for updating heat
    @param tau: product of capacitance and epsilon
    @param epsilon: Margin of error
    @param inside_temp: The temperature inside the room at time t (Th(t) in equation)
    @param outside_temp: The outside temperature at time t (Te(t) in equation)
    @return: the updated heat of the room (Th(t + delta) in equation)
    """
    return inside_temp + (delta_t * -(inside_temp - outside_temp)) / tau


def get_tau(delta_t, delta_heat, inside_temp, outside_temp):
    """
    Calculates tau - the produce of the capacitance and the resistance
    @param delta_t: the time interval or time step for updating heat
    @param delta_heat: the change of heat measured in delta_t (Th(t + delta) in equation)
    @param inside_temp: The temperature inside the room at time t (Th(t) in equation)
    @param outside_temp: The outside temperature at time t (Te(t) in equation)
    @return: tau
    """
    # calculate the denominator
    denom = delta_heat - inside_temp
    # avoid divide by 0
    if denom == 0:
        # return 0, this will be prune later
        return 0
    else:
        return -(delta_t * (inside_temp - outside_temp)) / denom


def is_stable(delta_t, cap, res):
    """
    determines whether or not the model is stable according to delta < capacitance * resitance
    @param delta_t: the time interval or time step for updating heat
    @param cap: the capacitance of a room (Ch in equation)
    @param res: the resistance of a room (Rhe in equations)
    @return: boolean representing whether or not the model is stable
    """
    return delta_t < (cap * res)


def clean_data(data):
    """
    Removes all values <= 0 from data
    :param data: a list of tau values
    :return: a new list with values > 0
    """
    return [x for x in data if x > 0]


def infer_tau(room):
    """
    Uses data from the rooms to infer tau and epsilon for the whole data set
    @param room: a room object containing temps and timestamps
    @return the tau value for the room
    """
    # dt is determined to be 10 from data
    # we could calculate this from the data, but there are some weird timestamps that throw off calculations.
    dt = 10
    # list to store all calculated capacitance for a particular room
    all_tau = []
    for i in range(len(room.temps) - 1):
        all_tau.append(get_tau(
            dt,
            room.temps[i + 1][1],
            room.temps[i][1],
            room.temps[i][2]
        ))

    # remove all values <= 0, since they are not useful
    all_tau = clean_data(all_tau)

    # check to make sure the node actually had readings
    if all_tau:
        # calculate the mean tau
        tau = sum(all_tau) / len(all_tau)
        # epsilon is the difference between dt and tau. add .5 to consider stability condition
        return tau
    else:
        return None

def get_b_tau(room_nums):
    """
    evaluates tau for the entire building
    @param room_nums: a list of room objects containing temps and timestamps
    @return the tau value for the building
    """
    return_list = []
    for r in room_nums:
        # get tau for each room type
        # and place in in list with node number
        temp = infer_tau(r)
        return_list.append([r.room_num,temp])
    total = 0
    # weight each room type by how many rooms there are
    # in math building of that type
    for x in return_list:
        if x[0] == '7':
            total = total + x[1]*28
        if x[0] == '9':
            total = total + x[1]*9
        if x[0] == '10':
            total = total + x[1]*10
        if x[0] == '19':
            total = total + x[1]*9
    # divide by the total number of rooms
    return total
    



