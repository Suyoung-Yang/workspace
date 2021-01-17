# divide
def mergesort(S):
    n = len(S)
    if (n<=1):
        return S
    else:
        mid = n // 2
        U = mergesort(S[0:mid])
        V = mergesort(S[mid:n])
        return merge(U,V)
# 한번 확인해볼까요?
# conquer 27, 10
def merge(U,V):
    A = []
    i = j = 0
    while(i<len(U) and j < len(V)):
        if(U[i] < V[j]):
            A.append(U[i])
            i += 1
        else:
            A.append(V[j])
            j += 1
        print(U,V)

    if (i <len(U)):
        A += U[i:len(U)]
    else:
        A += V[j:len(V)]
    print(A)
    return A

S1 = [27, 10, 12, 20, 25, 13, 15, 22]
S2 = S1[0:4]
print(S2)
S3 = S1[4:len(S1)]
print(S3)
mergesort(S1)
merge(S2,S3)
