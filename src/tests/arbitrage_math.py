Ts = float(input("Total Stake : "))
w1 = float(input("Weight 1 : "))
w2 = float(input("Weight 2 : "))

def WeightedAmount(w):
    return Ts * (w / (w1 + w2))

A = WeightedAmount(w2)
B = WeightedAmount(w1)

print("A = " + str(A))
print("B = " + str(B))
