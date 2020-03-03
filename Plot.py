import math
import matplotlib.pyplot as plt

prime =[]
y_val = []
def reverse_binary(num):
    b= str(bin(num))[2:]
    return num-int(("".join(reversed(b))),2)


for i in range(2,100000):
    is_prime = True
    for e in range(2,i):
        if (i%e==0):
            is_prime = False
            break
    if is_prime:
        prime.append(i)
        y_val.append(reverse_binary(i))


plt.plot(prime,y_val)
plt.show()