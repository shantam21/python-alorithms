def percentile_shan(data, percentile):
    k = len(data)
    data.sort()
    val = k*percentile/100
    val = [(math.ceil(val) - 1) if val!= 0 else math.ceil(val)]
    return data[val[0]]


arr = [1,100,9,5,6]

percentile_shan(arr,50)