def calc_cartesian_product(ranges):
    points = [[]]
    cp = [[]]
    for i in range(len(ranges)):
        points = list(cp)
        cp = []
        for j in points:
            for k in ranges[i]:
                new_j = list(j)
                new_j.append(k)
                cp.append(new_j)
    return cp

print(calc_cartesian_product([['a'],[1,2,3],['Y','Z']]))


