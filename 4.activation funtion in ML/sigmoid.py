import math
def sigmoid_funtion(data):
    result = []
    for d in data:
        result.append(1/(1+math.exp(-d)))
    return result

data = [1,5,-4,3,-2]
result = sigmoid_funtion(data)
print(result)