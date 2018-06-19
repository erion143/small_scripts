def foo(mass, ind):
    if ind >= len(mass) - 2:
        return None
    else:
        return mass[ind+1] - mass[ind]


def bar(vols, speeds):
    vols_ = [0]
    for vol1, vol2 in zip(vols, vols[1:]):
        vols_.append(vol1 + (vol2 - vol1) / 2)
        
    times = [0]
    for vol1, vol2, speed in zip(vols_, vols_[1:], speeds):
        times.append(times[-1] + (vol2 - vol1) / speed)

    return vols_, times


def test():
    vols = [i * 20 + 30 for i in range(10)]
    speeds = [1] * 10
    v, t = bar(vols, speeds)
    print(vols)
    print(v)
    print(t)
    
test()
