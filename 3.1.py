import random
def create():
    a=[]
    s=0
    for i in range(0,4):
        a.append(input())
        # print(a)
        s+=int(a[i])
        s=s % 2
        #print(s)
    a.append(str(s))
    print(a,"begin connect \n")
    return a


def connect(b):

    error=10
    for i in range(0,len(b)):
        rand = random.randint(0, 100)
        if (rand<=error):
            if(b[i]==0):
                b[i]=1
            else:
                b[i]=0
    print(b,"end connect \n")
    return b

def receive(c):
    sum=0
    for i in range(0,len(c)):
        sum+=int(c[i])
    sum=sum % 2
    if (sum==0):
        print(sum," успешно")
    else:
        print(sum," ошибка")

b=create()
c=connect(b)
receive(c)