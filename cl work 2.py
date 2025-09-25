def div(n, i = 2):
    while(i*i <= n):
        if n%1 !=0:
            i+=1
        else:
            return [i] + div(n//i,i)
    return [n]
print(div(int(input())))
            