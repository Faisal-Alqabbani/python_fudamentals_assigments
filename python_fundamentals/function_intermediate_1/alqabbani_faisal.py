import random
def randInt(min=0,max=100):
    if min > max or max > 0:
        return "the max value must be greater than min and zero"
    num = random.randint(min,max)
    return num
print(randInt(min=12, max=10))
