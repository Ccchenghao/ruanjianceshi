def hanshu(x):
    for i in range(2,x):
        if x % i ==0:
            return False
list1=[str(j) for j in range(10,20000)]
sum=[]

for a in list1:
    x=a[::-1]
    x=int(x)
    a=int(a)
    if hanshu(x) is not False:
        if hanshu(a) is not False:
            sum.append(a)
jishu=0
for d in sum:
    print(d,end='')
    jishu = jishu + 1
    if jishu%5==0:
        print()