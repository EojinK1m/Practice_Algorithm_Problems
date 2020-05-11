#https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    truck_weights = truck_weights[::-1]
    answer = 0
    weight_of_bridge = 0
    bridge = []

    while (truck_weights or bridge):
        for truck in bridge:
            if (truck[0] <= 0):
                weight_of_bridge -= truck[1]
                bridge.remove(truck)

        try:
            if (weight >= weight_of_bridge + truck_weights[-1]):
                bridge.append([bridge_length, truck_weights.pop()])
                weight_of_bridge += bridge[-1][1]
        except:
            pass
        for truck in bridge:
            truck[0] -= 1

        answer += 1

    return answer