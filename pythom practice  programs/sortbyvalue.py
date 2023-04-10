d = {45: 3453, 67: 567456, 12: 686786, 34: 23, 129: 1, 0: 67}

def get_value(item):
    return item[1]

sorted_d = dict(sorted(d.items(), key=get_value))

print(sorted_d)