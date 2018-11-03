import numpy as np
a=np.array([10,20,30,40])   # array([10, 20, 30, 40])
b=np.arange(4)              # array([0, 1, 2, 3])

c=a-b  # array([10, 19, 28, 37])
# print(c)
c=a+b   # array([10, 21, 32, 43])
# print(c)
c=a*b   # array([  0,  20,  60, 120])
# print(c)
c=b**2  # array([0, 1, 4, 9])
# print(c)
c=10*np.sin(a) # array([-5.44021111,  9.12945251, -9.88031624,  7.4511316 ])
# print(c)
# print(b<3)# array([ True,  True,  True, False], dtype=bool)

# dot
a=np.array([[1,1],
            [0,1]])
b=np.arange(4).reshape((2,2))
# print(a)
# print(b)
c_dot = np.dot(a,b)
# print(c_dot)
c_dot_2 = a.dot(b)
# print(c_dot_2)

a=np.random.random((2,4))
# print(a)
# array([[ 0.94692159,  0.20821798,  0.35339414,  0.2805278 ],
#       [ 0.04836775,  0.04023552,  0.44091941,  0.21665268]])
# print(np.sum(a))   # 4.4043622002745959
# print(np.min(a))  # 0.23651223533671784
# print(np.max(a))   # 0.90438450240606416

# print("a =",a)
# a = [[ 0.23651224  0.41900661  0.84869417  0.46456022]
# [ 0.60771087  0.9043845   0.36603285  0.55746074]]

# print("sum =",np.sum(a,axis=1))
# sum = [ 1.96877324  2.43558896]

# print("min =",np.min(a,axis=1))
# min = [ 0.23651224  0.41900661  0.36603285  0.46456022]

# print("max =",np.max(a,axis=1))
# max = [ 0.84869417  0.9043845 ]