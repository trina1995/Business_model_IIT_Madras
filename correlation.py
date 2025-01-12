def corr(data1, data2):
    n = data1.size

    sum1 = 0.
    sum2 = 0.
    for i in range(n):
        sum1 += data1[i]
        sum2 += data2[i]
    mean1 = sum1 / n
    mean2 = sum2 / n

    var_sum1 = 0.
    var_sum2 = 0.
    product = 0.
    for i in range(n):
        var_sum1 += (data1[i] - mean1) ** 2
        var_sum2 += (data2[i] - mean2) ** 2
        product += (data1[i] * data2[i])

    std1 = pow((var_sum1 / n),0.5)
    std2 = pow((var_sum2 / n),0.5)
    product =product/n

    return (product - mean1 * mean2) / (std1 * std2)