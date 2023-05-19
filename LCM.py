import math
numbers = map(int, input(). split())
lcm = math.lcm(*numbers)
print(lcm)