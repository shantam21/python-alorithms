#  naive appraoch to find the longest substring

X = "geeksforgeeksrocks"
Y = "nogeeksyesforgeeksnoforgeeksrocks"

X_substrings =[]
for i in range(len(X)):
    X_substrings.append(X[i:])
    X_substrings.append(X[:i+1])
# print(X_substrings)

len_longest_substring=0
for ss1 in X_substrings:
    for i in range(len(Y)): 
        ss2 = Y[i:]
        j=0
        # print(ss1,ss2)
        
        while((j<len(ss1)) & (j<len(ss2)) ) :
            if (ss1[j]==ss2[j]) :
                j=j+1
            else:
                break
        len_longest_substring = max(len_longest_substring, j)

print(len_longest_substring)