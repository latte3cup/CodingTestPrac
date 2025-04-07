def solution(players, callings):
    name_to_idx = {name: i for i, name in enumerate(players)}

    for name in callings:
        i = name_to_idx[name]         
        if i == 0:
            continue 

        front = players[i - 1]
        players[i - 1], players[i] = players[i], players[i - 1]

        name_to_idx[name] = i - 1
        name_to_idx[front] = i

    return players