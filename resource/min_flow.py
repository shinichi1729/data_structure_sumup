def min_cost_flow(V, cap, cost, f):
    reversed_cap = [[0 for _ in range(V)] for _ in range(V)]
    reversed_cost = [[-cost[j][i] for j in range(V)] for i in range(V)]
    previous = [-1] * V
    res, INF = 0, 1001001001
    while f > 0:
        dist = [INF] * V
        dist[0] = 0
        update = True
        while update:
            update = False
            for v in range(V):
                if dist[v] == INF:
                    continue
                for nxt_v in range(V):
                    if cap[v][nxt_v] == 0:
                        pass
                    elif dist[nxt_v] > dist[v] + cost[v][nxt_v]:
                        dist[nxt_v] = dist[v] + cost[v][nxt_v]
                        previous[nxt_v] = v
                        update = True
                    if reversed_cap[v][nxt_v] == 0:
                        pass
                    elif dist[nxt_v] > dist[v] + reversed_cost[v][nxt_v]:
                        dist[nxt_v] = dist[v] + reversed_cost[v][nxt_v]
                        previous[nxt_v] = v
                        update = True
        if dist[V-1] == INF:
            return None, -1
        delta, t = f, V-1
        while t > 0:
            if cap[previous[t]][t]:
                delta = min(delta, cap[previous[t]][t])
            else:
                delta = min(delta, reversed_cap[previous[t]][t])
            t = previous[t]
        f, res = f-delta, res+delta*dist[V-1]
        t = V-1
        while t > 0:
            if cap[previous[t]][t]:
                cap[previous[t]][t] -= delta
                reversed_cap[t][previous[t]] += delta
            else:
                cap[t][previous[t]] += delta
                reversed_cap[previous[t]][t] -= delta
            t = previous[t]
    return reversed_cap, res

def main():
    # data load
    V = int(input("頂点数を入力:"))
    print("上限容量を行列の形で入力:(辺がない場合0)")
    capacity = [list(map(int, input().split())) for _ in range(V)]
    print("コストを行列の形で入力:(辺がない場合0)")
    cost = [list(map(int, input().split())) for _ in range(V)]
    flow = int(input("流したい量:"))

    flow_net, min_cost = min_cost_flow(V, capacity, cost, flow)
    if flow_net is None:
        print("Impossible")
        return

    flow_net = [x for x in zip(*flow_net)]
    print("=" * 30)
    print("最小費用流:")
    print(*flow_net, sep='\n')
    print("最小費用:", min_cost)


if __name__ == '__main__':
    main()

