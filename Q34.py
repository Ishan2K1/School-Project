d={}
for i in range(1,7):
    for j in range(1,7):
             if (i+j) not in d:
            d[i+j] = [[i,j]]            
        else:
            [i+j].append([i,j])        
print(d)        
