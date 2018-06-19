def bar(vols, speeds):
    vols_ = [0]
    for vol1, vol2 in zip(vols, vols[1:]): # becouse volume's step can be less than first value 
        vols_.append(vol1 + (vol2 - vol1) / 2)
        
    times = [0]
    for vol1, vol2, speed in zip(vols_, vols_[1:], speeds):
        times.append(times[-1] + (vol2 - vol1) / speed)

    return vols_, times
