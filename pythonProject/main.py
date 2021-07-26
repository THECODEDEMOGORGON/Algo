import sys

values = [int(i) for i in sys.stdin.readline().split()]

N = values[0]
stats = dict.fromkeys(list(range(0, N)), 0)
matches_count = values[1]

players = set()

for c in range(matches_count):
    res = [int(i) for i in sys.stdin.readline().split()]
    A_results = int(res[0]) - int(res[1])
    B_results = int(res[1]) - int(res[0])

    ids = [int(i) for i in sys.stdin.readline().split()]
    players.update(ids)

    for i in ids[:5]:
        stats[i] = stats.get(i) + A_results
    for j in ids[5:]:
        stats[j] = stats.get(j) + B_results
    count = 0
    #
    # if stats[0] < 0:
    #     count += N - len(players)
    # for key in players:
    #     if stats[key] > stats[0]:
    #         count += 1
    values = sorted(stats.values())
    for value in values:
        if value > stats[0]:
            break
        count += 1

    print(N - count)
# N = int(input())
# matches_count
# stats = dict.fromkeys(list(range(0, N)), 0)
# print(stats)