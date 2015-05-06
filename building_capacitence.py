from model import *

def get_capacitence(room_nums):
    return_list = []
    for r in room_nums:
        temp = infer_vars(r)
        return_list.append([r.room_num,temp[0]])
    total = 0
    for x in return_list:
        if x[0] == '7':
            total = total + x[1]*28
        if x[0] == '9':
            total = total + x[1]*9
        if x[0] == '10':
            total = total + x[1]*10
        if x[0] == '19':
            total = total + x[1]*9
    cap = total/56
    return cap


