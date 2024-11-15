"""Point Sorting"""
def sort_point(points):
    """sort_point"""
    return sorted(points, key = lambda p: (p[0]+p[1], -p[1]))

def main(data = int(input())):
    """Point Sorting"""
    result = []
    for _ in range(data):
        datas = int(input())
        points = []
        for _ in range(datas):
            x, y = map(int, input().split())
            points.append((x, y))
        sorted_point = sort_point(points)
        for x, y in sorted_point:
            result.append(f"{x} {y}")
    print("\n".join(result))
main()
