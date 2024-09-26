import random
def create_pac():
    hexcode = "4e656b7261736f76204e696b69746120566c6164696d69726f766963682031302e30362e32303033"#!менять текст
    a = []
    new = []
    # делаем двоичный код с пробелами
    for i in range(0, len(hexcode), 2):

        chet=0
        elem = hexcode[i] + hexcode[i + 1]
        n = int(elem, 16)
        bStr = ''
        while n > 0:
            bStr = str(n % 2) + bStr
            n = n >> 1

        for j in range(0,len(bStr)):
            if int(bStr[j]) ==1:

                chet+=1

        # подгоняем каждый символ под 16 бит + контрольный бит


        bStr = "0" + bStr #!менять формат пакета
        if chet%2==0:
            bStr+="1"
        else:
            bStr+="0"
        print(len(bStr))
        a.append(bStr)
        new.append(bStr)
    print("create: \n",a,"\n")
    sss=[a,new]
    return sss
def connect(b):
    for j in range(0,len(b)):
        res_con=[]
        error=10 #!менять процент ошибки
        #если не повезло то бит инвертируется сразу в массиве
        new_elem = ''
        for i in range(0,len(b[j])):

            rand = random.randint(1, 100)
            if (rand<=error):
                if (b[j][i])=="1":
                    new_elem +="0"
                else:
                    new_elem +="1"

            else:
                new_elem+=b[j][i]
        b[j] = new_elem

    print("end connect \n",b,"\n")
    return b
def receive(b,c):
    all_pac=len(c)
    err_pac=0
    nice_pac=0
    for j in range(0,len(c)):
        sum = 0
        for i in range(0,len(c[j])-1):
            #print(c[j][i])
            sum+=int(c[j][i])
        sum=sum % 2
        if b[j]==c[j]:
            nice_pac+=1
        if int(c[j][len(c[j])-1])==sum:
            err_pac+=1
        #print(c[j][len(c[j]) - 1],sum)


        #print(c[j][len(c[j]) - 1], " ",sum)
    print(nice_pac," ",err_pac," ",all_pac)
    print((nice_pac+err_pac)/all_pac*100,"% успешных или выявленных\n",(1/9),"избыточность")



sss=create_pac()
c=connect(sss[0])

receive(sss[1],c)