#! 1d List:
L = [1, 2, 3, 4, 5]



#! 2d List:
M = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
    ]

#! 3d List:
N = [
    [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ],
    [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ],
    [
        [1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]
    ]
]


#^ Printing The List Data:
#! 1D:
#? Index:
# for i in range(len(L)):
    # print(L[i])

#? Element:
for i in L:
    print(i, end=" ")


print("\n----------------")
#! 2D:
for i in range(len(M)):
    for j in range(len(M[i])):
        print(M[i][j], end=" | ")
    print()


print("\n----------------")
#! 3D:
for i in range(len(N)):
    for j in range(len(N[i])):
        print()
        for k in range(len(N[i][j])):
            print(N[i][j][k], end=" | ")
    print()