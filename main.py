# 1. print table for any number input by user
'''
n = int(input("enter number: "))
for i in range(1,11):
    print(f"{n}x{i} = {n*i}")
'''
    
# 2. factorial of a number
'''
n = int(input("enter number: "))
f = 1
for i in range(1,n+1):      
    f = f*i
print(f"factorial of {n} is {f}")
'''

# 3. fibonacci
'''
a = int(input("enter 1st number: "))
b = int(input("enter 2nd number: ")) 
c = int(input("how many numbers you want series: "))
l= [a,b]
for i in range(1,c+1):
    l.append(l[i]+l[i-1])
print(l)
'''

