import numpy
def corr(data1, data2):
    n = data1.size
    mean1 = numpy.mean(data1)
    mean2 = numpy.mean(data2)

    var_sum1 = numpy.var(data1)
    var_sum2 = numpy.var(data2)
    product = (data1-mean1)*(data2-mean2)

    std1 = pow((var_sum1),0.5)
    std2 = pow((var_sum2),0.5)
    cov =sum(product)/n

    return (cov) / (std1 * std2)
data1 = numpy.array( [1,2,4,3,1,6,7,5,4,6,7], int )
data2 = numpy.array( [1,2,4,3,1,6,7,5,4,6,7], int )
r=corr(data1, data2)
print('r=', r)