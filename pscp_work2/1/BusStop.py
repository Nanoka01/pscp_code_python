"""BusStop I"""
def main():
    """BusStop I"""
    total = int(input())
    station = int(input())
    in_bus, passenger = [], []
    current_station = None
    count = 0
    for _ in range(1,station+1) :
        passenger.append(input().split())
    passenger.sort(key=lambda x: int(x[0]))
    for i in range(station) :
        current_station = passenger[i][1:]
        current_station = [x for x in current_station if int(x) > i]
        while passenger[i][0] in in_bus :
            in_bus.remove(passenger[i][0])
            count += 1
        while len(in_bus) < total and current_station :
            in_bus.append(current_station.pop(s0))
    print(count)
main()
