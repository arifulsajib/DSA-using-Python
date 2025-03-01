# Used to describe the performance of an algorithm
# Runtime complexity of a method

# O(1)- Constant (As the input grows, the runtime complexity is constant)
print("Hey there, this is Sajib");

# O(n) - Linear (As the input grows, the runtime complexity is linearly grows)
numbers = [1,2,3,4]
for x in numbers:
    print(x)

# O(n^2) - Quadratic (As the input grows, the runtime grows in Quadratic time)
numbers2 = [5,6,7,8]
for x in numbers:
    for y in numbers2:
        print(x,y)

# O(log n) - Logarithmic (As the input grows, the runtime grows slowly at some point, Efficient)

# O(2^n) - Exponential (opposite of logarithmic)