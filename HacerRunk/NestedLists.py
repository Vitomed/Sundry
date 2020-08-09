from typing import List, Tuple


def get_sorted_names(ns: List[Tuple[str, float]]):
    ns.sort(key=lambda x: x[1])
    initial_value = ns[0][1]
    result_names_list = []

    for idx, value in enumerate(ns):
        if value[1] > initial_value:
            checked_score = value[1]
            started_idx = idx
            break

    for n_s in ns[started_idx:]:
        if n_s[1] == checked_score:
            result_names_list.append(n_s[0])
        else:
            break

    return sorted(result_names_list)


names_scores = [('Harry', 37.21), ('Berry', 37.21), ('Tina', 37.2), ('Akriti', 41), ('Harsh', 39)]
assert get_sorted_names(ns=names_scores) == ['Berry', 'Harry']
