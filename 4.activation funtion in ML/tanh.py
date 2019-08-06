import math

def tanh_funtion(data):
    result = []
    for d in data:
        result.append((2/(1+math.exp(-2*d))) - 1)
    return result
data = [1,5,-4,3,-2]
result = tanh_funtion(data)
print(result)