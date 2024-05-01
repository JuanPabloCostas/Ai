
    
def getMin( a, b ):
    if ( a < b ): return a
    return b

def getMaxArray( a ):
    max = 0
    for i in range(len(a)):
        if a[i] > max: max = a[i]
    
    return max

R = [
[0.2, 0.6, 1, 0.8],
[0.4, 0.7, 0.9, 0.8],
[0.5, 0.6, 0.9, 0.4],
[1, 0.8, 0.7, 0.5]
]

S = [
[0.7, 1, 0.7, 0.5, 0.3],
[0.4, 0.6, 1, 0.6, 0.6],
[0.2, 0.4, 0.6, 1, 0.6],
[0.1, 0.3, 0.5, 0.5, 1]
]

Max_Min = [[],
     [],
     [],
     [],
     ]

# Run for 8, 16, 25, 33
for k in range(4):

    # Run for 10, 20, 40, 80, 95
    for j in range(len(S[0])):
        
        # Get the max out of the mins
        list = []
        for i in range(len(R[0])):
            list.append( getMin( R[k][i], S[i][j]) )

        # Store in Max_Min the max out of the mins
        Max_Min[k].append(getMaxArray(list))

print("Max_Min:")
for i in range(len(Max_Min)):
    print(Max_Min[i])

print("")

Max_Prod = [
    [],
    [],
    [],
    []
]

# Run for 8, 16, 25, 33
for k in range(len(S)):

    # Run for 10, 20, 40, 80, 95
    for j in range(len(S[0])):
        
        # Get the max out of the products
        list = []
        for i in range(len(R[0])):
            list.append( round(R[k][i] * S[i][j], 2) )

        # Store in Max_Prod the max out of the products
        Max_Prod[k].append(getMaxArray(list))

print("Max_Prod:")
for i in range(len(Max_Prod)):
    print(Max_Prod[i])