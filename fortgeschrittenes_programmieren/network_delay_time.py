def networkDelayTime(times, n: int, k: int):
    seen = [False for _ in range(n)]
    time_dict = {x:[] for x in range(n)}
    res = 0

    for s, d, t in times:
        time_dict[s-1].append((d-1, t))

    q = [k-1]
    print(time_dict)

    while q:
        curr_node = q.pop(0)
        if seen[curr_node]:
            continue
        seen[curr_node] = True

        for _ in range(len(time_dict[curr_node])):
            d, t = time_dict[curr_node].pop(0)
            if seen[d]:
                continue
            res += t
            q.append(d)
    
    return res


def main():
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n = 4
    k = 2

    print(networkDelayTime(times, n, k))  # Output: 2

if __name__ == "__main__":
    main()
