def study_schedule(permanence_period, target_time):
    total_hits = 0
    if target_time is None:
        return None
    for i in range(len(permanence_period)):
        current_period = permanence_period[i]
        init_point = current_period[0]
        end_point = current_period[1]
        if type(init_point) is not int or type(end_point) is not int:
            return None
        current_range = range(init_point, end_point + 1)
        if current_range.__contains__(target_time):
            total_hits += 1
    return total_hits
    raise NotImplementedError


study_schedule([[10, 20], [20, 30], [30, 40]], 20)
